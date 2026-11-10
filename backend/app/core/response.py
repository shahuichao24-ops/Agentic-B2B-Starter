from typing import Generic, TypeVar, Optional, Any
from pydantic import BaseModel
from fastapi.responses import JSONResponse

T = TypeVar("T")

class ApiResponse(BaseModel, Generic[T]):
    code: int = 200
    message: str = "success"
    data: Optional[T] = None

def success_response(data: Any = None, message: str = "success", code: int = 200) -> dict:
    """标准成功响应"""
    return {
        "code": code,
        "message": message,
        "data": data
    }

def error_response(message: str = "error", code: int = 400, data: Any = None) -> JSONResponse:
    """标准错误响应"""
    return JSONResponse(
        status_code=code if 400 <= code <= 599 else 400,
        content={
            "code": code,
            "message": message,
            "data": data
        }
    )
