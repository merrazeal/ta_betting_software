from abc import ABC, abstractmethod

from services.pubsub.message import Message


class BaseAsyncExecutor(ABC):

    @abstractmethod
    async def initialize(self) -> None: ...

    @abstractmethod
    async def execute(self) -> None: ...

    @abstractmethod
    async def close(self) -> None: ...

    @abstractmethod
    async def run(self) -> None: ...
