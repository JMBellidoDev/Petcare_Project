from datetime import date

from model.entity.user import UserCreate
from model.entity.client import Client
from model.entity.vet import Vet
from model.entity.vet_entity import VetEntity
from model.entity.pet import Pet


import re

# Pattern de username
REGEX_USERNAME = r'^\w{1,20}$'

# Pattern de email
REGEX_EMAIL = r'^[A-Za-z0-9]+([\.\-_][A-Za-z0-9]+)*@[A-Za-z]+\.[A-Za-z.]+$'

# Pattern de name
REGEX_NAME = r'^[A-ZÁÉÍÓÚÀÈÌÒÙÄËÏÖÜa-záéíóúàèìòùäëïöü]+'

# Pattern national_id_document
REGEX_NATIONAL_ID_DOCUMENT = r'^[A-Za-z0-9]\d{7}[A-Za-z]$'

# Pattern de phone_number
REGEX_PHONE_NUMBER = r'^[6789]\d{8}$'

# Pattern del cif
REGEX_CIF = r'^[a-zA-Z]\d{7}[a-zA-Z]$'

# Pattern de breed
REGEX_BREED = r'^[\w\s]{1,50}$'

# Longitud máxima del nombre de un usuario
MAX_LENGTH_NAME_USER = 100

# Longitud máxima del nombre de una mascota
MAX_LENGTH_NAME_PET = 30

# Longitud máxima del email
MAX_LENGTH_EMAIL = 80

# Longitud máxima de address
MAX_LENGTH_ADDRESS = 255

# Longitud máxima del chip o número identificativo del animal
MAX_LENGTH_CHIP = 15

# Tipos posibles de animal que acepta la aplicación
POSIBLE_TYPES = ["dog", "cat", "ferret", "horse", "bird", "rabbit"]




def check_user(user: UserCreate) -> bool:
  """
  Verifica que el usuario dado por parámetro cumple todos los requisitos para ser correcto

  Args:
    user (UserCreate): Usuario aportado. Debe cumplir:
      - username: debe contener únicamente letras o números, sin símbolos (excepto _), con una longitud máxima de 20 caracteres
      - email: debe tener el formato estándar de email, es decir, debe cumplir un pattern de email. longitud de hasta 80 caracteres

  Returns:
    bool: Indica si es correcto o no
  """

  return (re.match(REGEX_USERNAME, user.username) and re.match(REGEX_EMAIL, user.email) 
    and len(user.email) <= MAX_LENGTH_EMAIL
  )

def check_name(name: str) -> bool:
  """
  Verifica que un nombre está compuesto únicamente por espacios y letras, de una longitud no mayor a 100 caracteres
  """

  return all(re.match(REGEX_NAME, element) for element in re.split(r'\s+', name)) and len(name) <= MAX_LENGTH_NAME_USER


def check_client(client: Client) -> bool:
  """
  Verifica que el cliente cumple con todos los requisitos para ser correcto

  Args:
    client (Client): cliente aportado. Debe cumplir:
      - Todo requisito como usuario
      - name: Debe estar compuesto únicamente por letras y espacios, con una longitud no mayor a 100 caracteres
      - national_id_document: Debe cumplir con el patrón del NIF/NIE
      - birthdate: Debe ser una fecha anterior a la fecha actual
      - address: Debe tener una longitud no mayor a 255 caracteres
      - phone_number: Debe estar compuesto por 9 dígitos, siendo el primero un número entre el 6 y el 9

  Returns:
    bool: Indica si es correcto o no
  """

  return (
    check_user(UserCreate(
      username = client.username,
      email = client.email))
    
    and check_name(client.name)
    and re.match(REGEX_NATIONAL_ID_DOCUMENT, client.national_id_document)
    and re.match(REGEX_PHONE_NUMBER, client.phone_number)
    and len(client.address) <= MAX_LENGTH_ADDRESS
    and client.birthdate < date.today()
  )


def check_vet(vet: Vet) -> bool:
  """
  Verifica que el cliente cumple con todos los requisitos para ser correcto

  Args:
    client (Client): cliente aportado. Debe cumplir:
      - Todo requisito como usuario
      - name: Debe estar compuesto únicamente por letras y espacios, con una longitud no mayor a 100 caracteres
      - national_id_document: Debe cumplir con el patrón del NIF/NIE
   
  Returns:
    bool: Indica si es correcto o no
  """

  return (
    check_user(UserCreate(
      username = vet.username, 
      email = vet.email,))
    
    and check_name(vet.name)
    and re.match(REGEX_NATIONAL_ID_DOCUMENT, vet.national_id_document)
  )


def check_vet_entity(vet_entity: VetEntity) -> bool:
  """
  Verifica que la entidad veterinaria cumple con todos los requisitos para ser correcta

  Args:
    vet_entity (VetEntity): entidad veterinaria aportada. Debe cumplir:
      - Todo requisito como usuario
      - cif: Debe comenzar por una letra, seguida de 7 dígitos y, por último, una letra de control
      - name: Debe estar compuesto únicamente por letras y espacios, con una longitud no mayor a 100 caracteres
      - address: Debe tener una longitud no mayor a 255 caracteres
      - phone_number: Debe estar compuesto por 9 dígitos, siendo el primero un número entre el 6 y el 9

  Returns:
    bool: Indica si es correcto o no
  """
  return (
    check_user(UserCreate(
      username = vet_entity.username,
      email = vet_entity.email))
    
    and check_name(vet_entity.name)
    and re.match(REGEX_CIF, vet_entity.cif)
    and re.match(REGEX_PHONE_NUMBER, vet_entity.phone_number)
    and len(vet_entity.address) <= MAX_LENGTH_ADDRESS
  )

def check_pet(pet: Pet) -> bool:
  """
  Verifica que la mascota cumple todos los requisitos para ser correcta

  Args:
    pet (Pet): Mascota aportada. Debe cumplir:
      - chip_number: Número de chip de una longitud menor o igual a 15
      - type: Tipo de mascota: dog, cat, rabbit, ferret, horse, bird
      - breed: Debe contener únicamente letras y espacios
      - name: Debe estar compuesto únicamente por letras y espacios, con una longitud no mayor a 30 caracteres
  """

  return (
    len(pet.chip_number) <= MAX_LENGTH_CHIP
    and pet.type in POSIBLE_TYPES
    and re.match(REGEX_BREED, pet.breed)
    and re.match(REGEX_NAME, pet.name) and len(pet.name) <= MAX_LENGTH_NAME_PET
    and pet.birthdate <= date.today()
  )