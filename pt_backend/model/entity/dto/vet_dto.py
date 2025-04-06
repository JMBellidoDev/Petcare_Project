
from pydantic import BaseModel

from model.entity.vet_entity import VetEntity

class VetDto(BaseModel):
  """
  Veterinario DTO
  No es obligatorio que dicho veterinario esté asociado a una entidad veterinaria, puesto que puede ser autónomo
  """

  id: int
  name: str | None = None
  vet_entity: VetEntity | None = None