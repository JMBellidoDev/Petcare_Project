
from model.entity.user import UserCreate

from model.entity.dto.vet_entity_dto import VetEntityDto

class Vet(UserCreate):
  """
  Veterinario almacenado en el sistema, el cual tendrá acceso a la modificación de relaciones entre usuarios 
  y mascotas, además de poder generar informes y citas.
  No es obligatorio que dicho veterinario esté asociado a una entidad veterinaria, puesto que puede ser autónomo
  """

  national_id_document: str | None = None
  name: str | None = None
  registration_number: str | None = None
  vet_entity: VetEntityDto | None = None