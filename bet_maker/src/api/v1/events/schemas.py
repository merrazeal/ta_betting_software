from decimal import Decimal

from common.enums import EventState
from common.schemas import StateMixin, UUIDMixin


class Event(UUIDMixin, StateMixin):
    coefficient: Decimal
    deadline: int | None
