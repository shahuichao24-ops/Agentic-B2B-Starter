from datetime import datetime, timezone
from typing import Optional
from sqlmodel import SQLModel, Field
from app.core.tenant import get_current_tenant

def utc_now() -> datetime:
    return datetime.now(timezone.utc)

class BaseModel(SQLModel):
    """
    SaaS 核心审计与多租户基类：
    所有业务表必须继承此类，确保天然具备审计、软删除与租户隔离能力。
    """
    id: Optional[int] = Field(default=None, primary_key=True, description="主键 ID")
    created_at: datetime = Field(default_factory=utc_now, nullable=False, description="创建时间")
    updated_at: datetime = Field(default_factory=utc_now, nullable=False, description="最后更新时间")
    is_deleted: bool = Field(default=False, index=True, nullable=False, description="软删除标记（0未删，1已删）")
    tenant_id: str = Field(default_factory=get_current_tenant, index=True, nullable=False, description="租户标识")
