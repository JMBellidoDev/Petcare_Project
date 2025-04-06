from pydantic import BaseModel

class VetEntityDto(BaseModel):
  """
  Entidad veterinaria DTO
  """

  id: int | None = None
  name: str | None = None