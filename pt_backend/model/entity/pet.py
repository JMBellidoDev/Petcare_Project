from datetime import date
from typing import Optional

from model.entity.dto.client_dto import ClientDto

from pydantic import BaseModel

class Pet(BaseModel):
  """
  DTO de mascotas del sistema.
  Incluirá toda la información relacionada con la mascota
  """

  id: int | None = None
  chip_number: str
  type: str
  breed: str
  name: str
  birthdate: date
  alive: bool
  castrated: bool
  show: bool | None = None
  image: str | None = None
  clients: list[ClientDto] | None = None

  class Config:
    orm_mode = True