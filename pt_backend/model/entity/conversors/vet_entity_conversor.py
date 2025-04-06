
from model.tables import tables
from model.entity import vet_entity

def table_to_entity(table_vet_entity: tables.VetEntity) -> vet_entity.VetEntity:
  """
  Transforma un objeto VetEntity de la DB en un objeto VetEntity como entidad

  Args:
    table_vet_entity (tables.VetEntity): Entidad veterinaria de la DB

  Returns: 
    client.Client: Entidad veterinaria
  """

  return vet_entity.VetEntity(
    id = table_vet_entity.id,
    username = table_vet_entity.username,
    hashed_password = table_vet_entity.hashed_password,
    email = table_vet_entity.email,
    role = table_vet_entity.role,
    enabled = table_vet_entity.enabled,
    name = table_vet_entity.name,
    cif = table_vet_entity.cif,
    address = table_vet_entity.address,
    phone_number = table_vet_entity.phone_number
  )

def entity_to_table(vet_entity: vet_entity.VetEntity) -> tables.VetEntity:
  """
  Transforma un objeto VetEntity entidad en un objeto VetEntity de la DB

  Args:
    vet_entity (vet_entity.VetEntity): Entidad veterinaria

  Returns: 
    tables.Client: Entidad veterinaria de la DB
  """

  return tables.VetEntity(
    id = vet_entity.id,
    username = vet_entity.username,
    hashed_password = vet_entity.hashed_password,
    email = vet_entity.email,
    role = vet_entity.role,
    enabled = vet_entity.enabled,
    name = vet_entity.name,
    cif = vet_entity.cif,
    address = vet_entity.address,
    phone_number = vet_entity.phone_number
  )