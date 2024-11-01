from abc import ABC, abstractmethod


class HealthyInterface(ABC):

    def get_healty_check(self) -> dict:
        pass