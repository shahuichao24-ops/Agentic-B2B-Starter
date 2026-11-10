from fastapi import APIRouter
from app.api.v1.endpoints import suppliers

api_router = APIRouter()

# 挂载业务模块路由
api_router.include_router(suppliers.router, prefix="/suppliers", tags=["服务商准入合规"])
