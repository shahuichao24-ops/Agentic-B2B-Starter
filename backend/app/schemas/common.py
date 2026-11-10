from typing import Generic, TypeVar, List
from pydantic import BaseModel, Field
import math

T = TypeVar("T")

class PaginationParams(BaseModel):
    page: int = Field(default=1, ge=1, description="当前页码（从 1 开始）")
    page_size: int = Field(default=20, ge=1, le=100, description="每页条数（默认 20，上限 100）")

class PaginatedData(BaseModel, Generic[T]):
    items: List[T] = Field(description="列表数据项")
    total: int = Field(description="符合条件的总条数")
    page: int = Field(description="当前页码")
    page_size: int = Field(description="每页条数")
    total_pages: int = Field(description="总页数")

    @classmethod
    def create(cls, items: List[T], total: int, page: int, page_size: int) -> "PaginatedData[T]":
        total_pages = math.ceil(total / page_size) if page_size > 0 else 0
        return cls(
            items=items,
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages
        )
