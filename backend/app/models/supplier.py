from enum import Enum
from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel
from app.models.base import BaseModel

class SupplierStatus(str, Enum):
    """服务商准入状态枚举（杜绝手写字符串）"""
    PENDING = "pending"     # 待审核
    APPROVED = "approved"   # 已通过/合规
    REVISION = "revision"   # 需补正
    REJECTED = "rejected"   # 已驳回

class Supplier(BaseModel, table=True):
    """服务商数据表"""
    __tablename__ = "suppliers"

    name: str = Field(index=True, nullable=False, description="企业名称")
    credit_code: str = Field(index=True, unique=True, nullable=False, description="统一社会信用代码")
    contact_person: str = Field(nullable=False, description="联系人姓名")
    contact_phone: str = Field(nullable=False, description="联系电话")
    status: SupplierStatus = Field(default=SupplierStatus.PENDING, index=True, nullable=False, description="准入审核状态")
    review_notes: Optional[str] = Field(default=None, description="审核意见/驳回原因")

# --- Pydantic DTO 模型（入参与出参契约） ---

class SupplierCreate(SQLModel):
    name: str = Field(..., min_length=2, max_length=100, description="企业名称")
    credit_code: str = Field(..., min_length=18, max_length=18, description="18位统一社会信用代码")
    contact_person: str = Field(..., min_length=2, max_length=30, description="联系人姓名")
    contact_phone: str = Field(..., min_length=11, max_length=15, description="联系电话")

class SupplierUpdate(SQLModel):
    contact_person: Optional[str] = None
    contact_phone: Optional[str] = None

class SupplierReview(SQLModel):
    status: SupplierStatus = Field(..., description="审核结论：approved / revision / rejected")
    review_notes: Optional[str] = Field(default=None, description="审核说明")

class SupplierRead(SQLModel):
    id: int
    name: str
    credit_code: str
    contact_person: str
    contact_phone: str
    status: SupplierStatus
    review_notes: Optional[str]
    created_at: datetime
    updated_at: datetime
