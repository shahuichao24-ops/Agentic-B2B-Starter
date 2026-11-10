from sqlmodel import SQLModel, create_engine, Session, select
from typing import Generator
from sqlalchemy import event, and_
from sqlalchemy.orm import with_loader_criteria
from app.core.config import settings
from app.core.tenant import get_current_tenant
from app.models.base import BaseModel

# SQLite 多线程模式配置
connect_args = {"check_same_thread": False} if settings.DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(
    settings.DATABASE_URL,
    echo=False,
    connect_args=connect_args
)

@event.listens_for(Session, "do_orm_execute")
def _auto_tenant_and_soft_delete_filter(execute_state):
    """
    会话级多租户与软删除自动过滤 Hook：
    对所有继承 BaseModel 的数据表，默认在底层注入当前请求的 tenant_id 与 is_deleted == False 过滤。
    支持在查询时通过 .execution_options(include_deleted=True) 或 (skip_tenant_filter=True) 精确控制。
    """
    if execute_state.is_select and not execute_state.is_column_load:
        skip_tenant = execute_state.execution_options.get("skip_tenant_filter", False)
        include_deleted = execute_state.execution_options.get("include_deleted", False)

        if skip_tenant and include_deleted:
            return

        curr_tenant = get_current_tenant()
        opts = []
        for model in BaseModel.__subclasses__():
            if getattr(model, "__tablename__", None):
                def make_criteria(cls):
                    conditions = []
                    if not skip_tenant:
                        conditions.append(cls.tenant_id == curr_tenant)
                    if not include_deleted:
                        conditions.append(cls.is_deleted == False)
                    return and_(*conditions) if conditions else True

                opts.append(
                    with_loader_criteria(
                        model,
                        make_criteria,
                        track_closure_variables=False
                    )
                )
        if opts:
            execute_state.statement = execute_state.statement.options(*opts)

def get_session() -> Generator[Session, None, None]:
    """FastAPI 依赖注入 Session"""
    with Session(engine) as session:
        yield session

def init_db():
    """初始化数据库表并注入基础种子数据"""
    # 提前导入所有业务模型，使 SQLModel.metadata 能够识别并创建所有数据表
    from app.models.supplier import Supplier, SupplierStatus

    SQLModel.metadata.create_all(engine)
    
    with Session(engine) as session:
        existing = session.exec(select(Supplier)).first()
        if not existing:
            demo_suppliers = [
                Supplier(
                    name="华东智造云计算科技有限公司",
                    credit_code="91330108MA28WXXX01",
                    contact_person="张经理",
                    contact_phone="13800000001",
                    status=SupplierStatus.APPROVED,
                    review_notes="资质齐全，通过准入合规审核"
                ),
                Supplier(
                    name="北京远见数智软件科技有限公司",
                    credit_code="91110105MA01XXXX02",
                    contact_person="李总监",
                    contact_phone="13900000002",
                    status=SupplierStatus.PENDING,
                    review_notes=None
                ),
                Supplier(
                    name="上海瀚海供应链管理有限公司",
                    credit_code="91310115MA1HXXXX03",
                    contact_person="王主管",
                    contact_phone="13700000003",
                    status=SupplierStatus.REVISION,
                    review_notes="缺少最新的营业执照增项核验凭证，请补正后重新提交"
                ),
                Supplier(
                    name="广州深蓝数字物流服务有限公司",
                    credit_code="91440101MA59XXXX04",
                    contact_person="赵代表",
                    contact_phone="13600000004",
                    status=SupplierStatus.REJECTED,
                    review_notes="经营范围不符合准入名录要求"
                ),
                Supplier(
                    name="深圳极光智能安全技术有限公司",
                    credit_code="91440300MA5EXXXX05",
                    contact_person="孙工",
                    contact_phone="13500000005",
                    status=SupplierStatus.APPROVED,
                    review_notes="已通过三级等保与信息安全合规认证"
                ),
            ]
            session.add_all(demo_suppliers)
            session.commit()
