from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.core.database import init_db
from app.core.tenant import TenantMiddleware
from app.api.v1.api import api_router
from app.core.response import error_response

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 服务启动：初始化数据库与种子数据
    init_db()
    yield
    # 服务关闭清理（如有）

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="面向企业级 B2B SaaS 的标准化后端框架，提供统一响应、规范分页、数据审计与自动接口文档。",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# 配置 CORS 跨域（支持前端 Vite 开发服务）
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 挂载多租户自动隔离拦截中间件
app.add_middleware(TenantMiddleware)

# 全局参数校验异常捕获（保证格式依然符合规范外壳）
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    first_error = exc.errors()[0]
    loc = " -> ".join([str(x) for x in first_error.get("loc", [])])
    msg = f"参数校验失败 [{loc}]: {first_error.get('msg')}"
    return error_response(message=msg, code=status.HTTP_422_UNPROCESSABLE_ENTITY, data=exc.errors())

# 数据库唯一性冲突与完整性约束异常捕获
from sqlalchemy.exc import IntegrityError
@app.exception_handler(IntegrityError)
async def integrity_exception_handler(request: Request, exc: IntegrityError):
    return error_response(message="数据冲突或已被占用（违反数据唯一性约束）", code=status.HTTP_400_BAD_REQUEST)

# HTTP 框架异常捕获（覆盖 RBAC 403 / 404 / 405 等，确保统一返回规范外壳）
from starlette.exceptions import HTTPException as StarletteHTTPException
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return error_response(message=str(exc.detail), code=exc.status_code)

# 挂载 API 路由
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/", tags=["系统根节点"])
def root():
    return {
        "status": "online",
        "project": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "docs": "/docs",
        "redoc": "/redoc"
    }
