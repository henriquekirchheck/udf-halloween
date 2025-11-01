from abc import ABC, abstractmethod


class Entity(ABC):
    @abstractmethod
    def init(
        self,
    ) -> None:
        pass

    @abstractmethod
    def process(self, delta: float) -> None:
        pass

    @abstractmethod
    def process_physics(
        self,
    ) -> None:
        pass
