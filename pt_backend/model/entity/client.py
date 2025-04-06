from datetime import date

from model.entity.user import UserCreate


class Client(UserCreate):
  """
  Cliente usuario de la entidad, el cual únicamente tendrá acceso a sus mascotas y a toda información relacionada con ellos

  Attributes:
    id (int): ID autogenerado de la DB para el usuario
    username (str): Nombre de usuario del sistema
    role (str): Role que posee el veterinario. Será 'client', 'vet' o 'vet_entity'
    name (str): Nombre completo real del usuario, o nombre de la entidad veterinaria
    email (str): Email del usuario
    enabled (bool): Booleano que indica si el usuario está activo actualmente
    hashed_password (str): Contraseña ya hasheada para el almacenamiento de la contraseña
    national_id_document (str): Documento nacional de identidad (NIF/NIE)
    birthdate (date): Fecha de nacimiento
    address (str): Dirección de residencia del usuario
    phone_number (str): Número de teléfono del usuario
  """

  national_id_document: str | None = None
  name: str | None = None
  birthdate: date | None = None
  address: str | None = None
  phone_number: str | None = None