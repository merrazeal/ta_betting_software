import asyncio
import logging

from core.config import settings
from services.pubsub.adapters.executor import BaseAsyncExecutor
from services.pubsub.adapters.subsciber import BaseAsyncSubscriber
from services.pubsub.message import Message


class AsyncConsumer:
    def __init__(
        self,
        subscriber: BaseAsyncSubscriber,
        task_executor: BaseAsyncExecutor,
        logger: logging.Logger = logging.getLogger(""),
    ) -> None:
        self.logger = logger
        self.subscriber = subscriber
        self.task_executor = task_executor

    async def run(self) -> None:
        while True:
            new_message: Message | None = await self.subscriber.receive()
            if new_message:
                self.logger.info(f"New message received: {new_message}")
                await self.task_executor.exe_queue.put(new_message)
            await asyncio.sleep(settings.message_poll_interval)

    async def consume(self) -> None:
        self.logger.info("Starting to consume messages")
        try:
            await self.task_executor.initialize()
        except Exception as e:
            self.logger.error(f"Executor initialized failed: {e}")
        else:
            self.logger.info("Executor initialized successfully")

        try:
            await self.subscriber.initialize()
        except Exception as e:
            self.logger.error(f"Subscriber initialized failed: {e}")
        else:
            self.logger.info("Subscriber initialized successfully")

        asyncio.create_task(self.run())
        asyncio.create_task(self.task_executor.run())

    async def close(self) -> None:
        await self.subscriber.close()
        await self.task_executor.close()
