import uuid

from common.schemas import InputData, Message


class MessageBuilder:
    def __init__(self, func_name) -> None:
        self.func_name = func_name

    def build(self, *args, **kwargs) -> Message:
        return Message(
            id=uuid.uuid4(),
            task_name=self.func_name,
            input_data=InputData(args=args, kwargs=kwargs),
        )
