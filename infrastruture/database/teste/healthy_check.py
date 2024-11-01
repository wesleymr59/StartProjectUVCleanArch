
from app.interfaces.healthyCheck.healthy_check import HealthyInterface


class TesteRepository(HealthyInterface):
    def get_healty_check(self) -> dict:
        return {"Message": "Healthy Check Ok"}