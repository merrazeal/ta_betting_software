import uuid
from decimal import Decimal

from pydantic import BaseModel, Field

from common.enums import EventState
from common.schemas import UUIDMixin


class Bet(UUIDMixin):
    state: EventState | None = None


class CreateBet(BaseModel):
    event_id: uuid.UUID
    amount: Decimal = Field(decimal_places=2, ge=0.01)
