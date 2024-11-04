import uuid

from pydantic import BaseModel

from common.enums import EventState


class UUIDMixin(BaseModel):
    id: uuid.UUID


class StateMixin(BaseModel):
    state: EventState

    class Config:
        use_enum_values = True
