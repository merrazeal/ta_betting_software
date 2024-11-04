import uuid
from typing import Any

from pydantic import BaseModel


class InputData(BaseModel):
    args: list[Any]
    kwargs: dict[str, Any]


class Message(BaseModel):
    id: uuid.UUID
    task_name: str
    input_data: InputData
