import uuid
from typing import Any

from pydantic import BaseModel, Field

from common.enums import EventState


class InputData(BaseModel):
    args: list[Any]
    kwargs: dict[str, Any]


class Message(BaseModel):
    id: uuid.UUID
    task_name: str
    input_data: InputData


class UUIDMixin(BaseModel):
    id: uuid.UUID


class Pagination(BaseModel):
    page_number: int = Field(default=1)
    page_size: int = Field(default=50)


class BaseEsParams(BaseModel):
    pagination: Pagination = Pagination(page_number=1, page_size=50)
    terms_filters: list[dict[str, Any]] = Field(default_factory=list)
    must_multimatch_search_query: list[dict[str, Any]] = Field(default_factory=list)
    sort: list[dict[str, Any]] = Field(default_factory=list)
    # ...


class StateMixin(BaseModel):
    state: EventState

    class Config:
        use_enum_values = True
