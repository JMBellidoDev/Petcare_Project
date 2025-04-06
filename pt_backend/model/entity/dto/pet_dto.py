from model.entity.dto.client_dto import ClientDto

from pydantic import BaseModel

class PetDto(BaseModel):
  """
  DTO de mascotas del sistema
  """

  id: int | None = None
  chip_number: str | None = None
  name: str | None = None
  clients: list[ClientDto] | None = None
