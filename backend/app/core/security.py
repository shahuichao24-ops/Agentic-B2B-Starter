from enum import Enum
from typing import List, Callable
from fastapi import Request, HTTPException, status, Depends
from app.core.response import error_response

class UserRole(str, Enum):
    """B 端三级标准角色枚举"""
    ADMIN = "admin"        # 系统管理员（全局全权）
    REVIEWER = "reviewer"  # 业务审核员（仅有查询与审核通过/驳回权）
    OPERATOR = "operator"  # 经办/录入员（仅有录入与本人数据查看权）

def get_current_role(request: Request) -> UserRole:
    """
    从请求头 X-User-Role 提取当前用户角色（原型与测试桩模式）。
    遵循 Fail-Closed 原则，未显式声明时默认为最低权限 OPERATOR。
    在生产环境中，此信息必须从校验通过的 JWT Token Claim 中获取。
    """
    raw_role = request.headers.get("X-User-Role", "operator").lower()
    try:
        return UserRole(raw_role)
    except ValueError:
        return UserRole.OPERATOR

def require_roles(allowed_roles: List[UserRole]) -> Callable:
    """
    权限切面防呆依赖注入：
    在路由上声明例如 dependencies=[Depends(require_roles([UserRole.ADMIN, UserRole.REVIEWER]))]
    若角色不匹配，自动拦截并抛出标准 403 结构。
    """
    def role_checker(role: UserRole = Depends(get_current_role)):
        if role not in allowed_roles:
            role_names = [r.value for r in allowed_roles]
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"权限不足：当前角色 [{role.value}] 无权执行此操作，所需权限角色: {role_names}"
            )
        return role

    return role_checker
