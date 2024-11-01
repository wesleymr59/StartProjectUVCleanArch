from app.entities.healthyCheck.Response.healthy_response import HealthyResponse
from app.usecases.healthyCheck.healthy_check import HealthyUseCase
from infrastruture.database.teste.healthy_check import TesteRepository


class HealthyComposer():
    @staticmethod
    def healthy_composer() -> HealthyResponse:
        testeRepository = TesteRepository()
        return HealthyUseCase(healthy_interface=testeRepository)