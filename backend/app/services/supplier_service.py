from typing import Optional
from sqlmodel import Session, select, func
from app.models.supplier import Supplier, SupplierCreate, SupplierUpdate, SupplierReview, SupplierStatus
from app.schemas.common import PaginationParams, PaginatedData
from app.models.base import utc_now

class SupplierService:
    @staticmethod
    def list_suppliers(
        session: Session,
        pagination: PaginationParams,
        status: Optional[SupplierStatus] = None,
        keyword: Optional[str] = None
    ) -> PaginatedData[Supplier]:
        """获取服务商分页列表"""
        query = select(Supplier).where(Supplier.is_deleted == False)

        if status:
            query = query.where(Supplier.status == status)
        if keyword:
            query = query.where(
                (Supplier.name.contains(keyword)) | 
                (Supplier.credit_code.contains(keyword)) |
                (Supplier.contact_person.contains(keyword))
            )

        # 统计总数
        count_query = select(func.count()).select_from(query.subquery())
        total = session.exec(count_query).one()

        # 分页排序（默认按创建时间倒序）
        offset = (pagination.page - 1) * pagination.page_size
        paged_query = query.order_by(Supplier.created_at.desc()).offset(offset).limit(pagination.page_size)
        items = list(session.exec(paged_query).all())

        return PaginatedData.create(
            items=items,
            total=total,
            page=pagination.page,
            page_size=pagination.page_size
        )

    @staticmethod
    def get_by_id(session: Session, supplier_id: int) -> Optional[Supplier]:
        """根据 ID 获取未删除的服务商"""
        query = select(Supplier).where(Supplier.id == supplier_id, Supplier.is_deleted == False)
        return session.exec(query).first()

    @staticmethod
    def get_by_credit_code(session: Session, credit_code: str, include_deleted: bool = False) -> Optional[Supplier]:
        """根据信用代码查询服务商"""
        query = select(Supplier).where(Supplier.credit_code == credit_code)
        if not include_deleted:
            query = query.where(Supplier.is_deleted == False)
        return session.exec(query).first()

    @staticmethod
    def create(session: Session, data: SupplierCreate) -> Supplier:
        """创建服务商"""
        supplier = Supplier.model_validate(data)
        supplier.status = SupplierStatus.PENDING
        session.add(supplier)
        session.commit()
        session.refresh(supplier)
        return supplier

    @staticmethod
    def review(session: Session, supplier: Supplier, review_data: SupplierReview) -> Supplier:
        """审核服务商准入状态流转"""
        supplier.status = review_data.status
        supplier.review_notes = review_data.review_notes
        supplier.updated_at = utc_now()
        session.add(supplier)
        session.commit()
        session.refresh(supplier)
        return supplier

    @staticmethod
    def soft_delete(session: Session, supplier: Supplier) -> bool:
        """软删除服务商"""
        supplier.is_deleted = True
        supplier.updated_at = utc_now()
        session.add(supplier)
        session.commit()
        return True
