

from starlette.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI
from typing import Any
from typing import Optional
from pydantic import BaseModel
from fastapi import Request


class ErrorResponse(BaseModel):
    status_code: int
    message: str
    details: Optional[dict[str, Any]] = None


def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "status_code": 422,
            "message": "Input format is wrong",
            "details": exc.errors()
        }
    )


def register_exception_handler(app: FastAPI):
    app.add_exception_handler(RequestValidationError,
                              validation_exception_handler)
