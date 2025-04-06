from datetime import datetime

from model.entity.dto.pet_dto import PetDto
from model.entity.dto.vet_dto import VetDto
from model.entity.dto.client_dto import ClientDto

from pydantic import BaseModel

class Appointment(BaseModel):
  """
  Cita veterinaria que incluirá toda la información referente a
  la cita, al igual que la información del resto de entidades relacionadas
  """

  id: int  | None = None
  pet: PetDto
  vet: VetDto
  client: ClientDto
  appointment_date: datetime

