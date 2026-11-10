from typing import Optional
from fastapi import APIRouter, Depends, Query, Path
from sqlmodel import Session, select
from app.core.database import get_session
from app.core.response import ApiResponse, success_response, error_response
from app.core.security import UserRole, require_roles
from app.models.supplier import (
    Supplier,
    SupplierStatus,
    SupplierCreate,
    SupplierReview,
    SupplierRead
)
from app.schemas.common import PaginationParams, PaginatedData
from app.services.supplier_service import SupplierService

router = APIRouter()

@router.get(
    "",
    response_model=ApiResponse[PaginatedData[SupplierRead]],
    summary="获取服务商分页列表"
)
def list_suppliers(
    page: int = Query(1, ge=1, description="当前页码"),
    page_size: int = Query(20, ge=1, le=100, description="每页条数"),
    status: Optional[SupplierStatus] = Query(None, description="状态筛选：pending/approved/revision/rejected"),
    keyword: Optional[str] = Query(None, description="关键词搜索（名称/信用代码/联系人）"),
    session: Session = Depends(get_session)
):
    pagination = PaginationParams(page=page, page_size=page_size)
    result = SupplierService.list_suppliers(session, pagination, status, keyword)
    return success_response(data=result)

@router.post(
    "",
    response_model=ApiResponse[SupplierRead],
    summary="创建/录入新服务商"
)
def create_supplier(
    data: SupplierCreate,
    session: Session = Depends(get_session)
):
    existing = SupplierService.get_by_credit_code(session, data.credit_code, include_deleted=True)
    if existing:
        if existing.is_deleted:
            return error_response(message=f"统一社会信用代码 {data.credit_code} 处于已归档状态，可调用恢复接口重新激活", code=400)
        return error_response(message=f"统一社会信用代码 {data.credit_code} 已存在，请勿重复录入", code=400)

    supplier = SupplierService.create(session, data)
    return success_response(data=supplier, message="服务商录入成功")

@router.get(
    "/{supplier_id}",
    response_model=ApiResponse[SupplierRead],
    summary="获取服务商详情"
)
def get_supplier_detail(
    supplier_id: int = Path(..., description="服务商主键 ID"),
    session: Session = Depends(get_session)
):
    supplier = SupplierService.get_by_id(session, supplier_id)
    if not supplier:
        return error_response(message="服务商不存在或已被移除", code=404)
    return success_response(data=supplier)

@router.post(
    "/{supplier_id}/review",
    response_model=ApiResponse[SupplierRead],
    summary="审核服务商准入状态",
    dependencies=[Depends(require_roles([UserRole.ADMIN, UserRole.REVIEWER]))]
)
def review_supplier(
    supplier_id: int = Path(..., description="服务商主键 ID"),
    review_data: SupplierReview = ...,
    session: Session = Depends(get_session)
):
    supplier = SupplierService.get_by_id(session, supplier_id)
    if not supplier:
        return error_response(message="服务商不存在", code=404)
    
    reviewed = SupplierService.review(session, supplier, review_data)
    return success_response(data=reviewed, message="审核结果提交成功")

@router.delete(
    "/{supplier_id}",
    response_model=ApiResponse[bool],
    summary="软删除服务商",
    dependencies=[Depends(require_roles([UserRole.ADMIN]))]
)
def delete_supplier(
    supplier_id: int = Path(..., description="服务商主键 ID"),
    session: Session = Depends(get_session)
):
    supplier = SupplierService.get_by_id(session, supplier_id)
    if not supplier:
        return error_response(message="服务商不存在", code=404)
    
    SupplierService.soft_delete(session, supplier)
    return success_response(data=True, message="服务商已移至回收站")

@router.post(
    "/{supplier_id}/restore",
    response_model=ApiResponse[SupplierRead],
    summary="从回收站恢复服务商",
    dependencies=[Depends(require_roles([UserRole.ADMIN]))]
)
def restore_supplier(
    supplier_id: int = Path(..., description="服务商主键 ID"),
    session: Session = Depends(get_session)
):
    query = select(Supplier).where(Supplier.id == supplier_id).execution_options(include_deleted=True)
    supplier = session.exec(query).first()
    if not supplier or not supplier.is_deleted:
        return error_response(message="未找到处于已删除状态的服务商", code=404)
    
    restored = SupplierService.restore(session, supplier)
    return success_response(data=restored, message="服务商已成功恢复")
