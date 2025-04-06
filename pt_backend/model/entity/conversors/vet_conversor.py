from model.DB.connection import SessionLocal

from model.entity import vet
from model.entity.dto.vet_entity_dto import VetEntityDto
from model.tables import tables

def table_to_entity(table_vet: tables.Vet) -> vet.Vet:
  """
  Transforma un objeto Vet de la DB en un objeto Vet como entidad

  Args:
    table_vet (tables.Vet): Veterinario de la DB
    with_vet_entity (bool): Indica si se debe convertir también la entidad veterinaria

  Returns: 
    vet.Vet: Veterinario entidad 
  """

  # Se asignan todos los valores
  return vet.Vet(
    id = table_vet.id,
    username = table_vet.username,
    hashed_password = table_vet.hashed_password,
    email = table_vet.email,
    role = table_vet.role,
    enabled = table_vet.enabled,
    name = table_vet.name,
    national_id_document = table_vet.national_id_document,
    registration_number = table_vet.registration_number,
    vet_entity = VetEntityDto(id = table_vet.vet_entity.id, name = table_vet.vet_entity.name) if table_vet.vet_entity_id != None else VetEntityDto()
  )


def entity_to_table(vet: vet.Vet) -> tables.Vet:
  """
  Transforma un objeto Vet en un objeto Vet de la DB

  Args:
    vet (vet.Vet): Veterinario entidad

  Returns: 
    tables.Vet: Veterinario de la DB
  """

  return tables.Vet(
    id = vet.id,
    username = vet.username,
    hashed_password = vet.hashed_password,
    email = vet.email,
    role = vet.role,
    enabled = vet.enabled,
    name = vet.name,
    national_id_document = vet.national_id_document,
    registration_number = vet.registration_number,
    vet_entity_id = vet.vet_entity.id if vet.vet_entity else None
  )

