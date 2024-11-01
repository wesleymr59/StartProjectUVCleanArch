from fastapi import APIRouter, Depends

from app.composers.healthy_check import HealthyComposer
from app.entities.healthyCheck.Response.healthy_response import HealthyResponse
from app.usecases.healthyCheck.healthy_check import HealthyUseCase


router = APIRouter()


@router.get("/healthy_check/")
def healthy_check( healthyUseCase: HealthyUseCase = Depends(HealthyComposer.healthy_composer)) -> HealthyResponse:
        return healthyUseCase.healthy_check()