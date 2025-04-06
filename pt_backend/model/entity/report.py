from datetime import datetime

from model.entity.dto.pet_dto import PetDto
from model.entity.dto.vet_dto import VetDto

from pydantic import BaseModel

class Report(BaseModel):
  """
  DTO de un informe veterinario
  """

  id: int  | None = None
  pet: PetDto
  vet: VetDto
  reason: str
  diagnosis: str
  treatment: str
  report_date: datetime = datetime.now()

