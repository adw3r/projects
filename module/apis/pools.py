import abc
from typing import NoReturn


class Pool:
    pool: list = []

    def __repr__(self):
        return self.pool_name

    def __init__(self, pool_name: str):
        self.pool_name = pool_name

    def __len__(self) -> int:
        return len(self.pool)

    @abc.abstractmethod
    def pop(self) -> str:
        ...

    @abc.abstractmethod
    def get_pool(self) -> NoReturn:
        ...
