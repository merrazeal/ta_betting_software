from abc import ABC, abstractmethod

from services.pubsub.message import Message


class BaseAsyncSubscriber(ABC):

    @abstractmethod
    async def initialize(self) -> None: ...

    @abstractmethod
    async def receive(self) -> Message | None: ...

    @abstractmethod
    async def close(self) -> None: ...
