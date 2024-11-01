from app.interfaces.healthyCheck.healthy_check import HealthyInterface


class HealthyUseCase():
    def __init__(self, healthy_interface: HealthyInterface) -> None:
        self.healthyRepo = healthy_interface

    def healthy_check(self):
        a = self.healthyRepo.get_healty_check()
        print(a)
        return a