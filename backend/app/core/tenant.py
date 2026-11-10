import contextvars
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

# 线程/协程安全的全局租户上下文（默认单租户为 "default"）
_tenant_context: contextvars.ContextVar[str] = contextvars.ContextVar("tenant_id", default="default")

def get_current_tenant() -> str:
    """获取当前请求所属的租户 ID"""
    return _tenant_context.get()

def set_current_tenant(tenant_id: str):
    """设置当前租户 ID"""
    _tenant_context.set(tenant_id)

class TenantMiddleware(BaseHTTPMiddleware):
    """
    多租户会话隔离中间件（原型验证与开发模式）：
    从请求头 X-Tenant-Id 提取租户标识，自动注入当前协程上下文供数据库 Hook 自动过滤。
    若未传则默认 fallback 到 'default'，确保单租户/本地开发零配置无感运行。
    
    【生产提示】：
    生产环境下租户身份必须从已签名的 JWT Token Claim 中获取，严禁直接信任未鉴权的 HTTP Header。
    """
    async def dispatch(self, request: Request, call_next):
        tenant_id = request.headers.get("X-Tenant-Id") or "default"
        token = _tenant_context.set(tenant_id)
        try:
            response: Response = await call_next(request)
            # 在响应头回传当前租户标识，便于前端感知
            response.headers["X-Tenant-Id"] = tenant_id
            return response
        finally:
            _tenant_context.reset(token)
