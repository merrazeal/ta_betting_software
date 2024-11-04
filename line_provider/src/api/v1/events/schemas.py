from decimal import Decimal

from common.schemas import StateMixin, UUIDMixin


class UpdateState(StateMixin): ...


class Event(UUIDMixin, StateMixin):
    coefficient: Decimal
    deadline: int | None = None

    class Config:
        use_enum_values = True


class CreateEvent(StateMixin):
    coefficient: Decimal
    deadline: int | None = None
