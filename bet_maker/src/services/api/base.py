from abc import ABC, abstractmethod


class BaseAPIService(ABC):
    @classmethod
    @abstractmethod
    def get_list(self) -> list[dict]: ...

    @classmethod
    @abstractmethod
    def get_detail_by_id(self, id: str) -> dict: ...

    # ...
