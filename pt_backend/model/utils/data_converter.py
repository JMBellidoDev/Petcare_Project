import re


def converter_national_id_document(national_id_document: str):
  """
  Convierte las letras del NIF/NIE a mayúscula

  Args:
    national_id_document (str): NIF/NIE

  Returns:
    str: El NIF/NIE con las letras en mayúscula
  """
  
  return national_id_document.upper()


def converter_name(name: str):
  """
  Transforma el nombre aportado, poniendo cada letra de comienzo de palabra en mayúscula
  y el resto en minúscula

  Args:
    name: Nombre a transformar

  Returns:
    str: Nombre con las condiciones ya establecidas
  """

  name_parts = re.split(r'\s+', name)
  return ' '.join(part.capitalize() for part in name_parts)


def converter_cif(cif: str):
  """
  Convierte las letras del CIF a mayúscula

  Args:
    cif (str): CIF

  Returns:
    str: El CIF con las letras en mayúscula
  """
  
  return cif.upper()


def converter_email(email: str):
  """
  Convierte las letras del email a minúscula

  Args:
    email (str): email

  Returns:
    str: El email con las letras en minúscula
  """
  
  return email.lower()


def converter_breed(breed: str):
  """
  Transforma la raza aportada, poniendo cada letra de comienzo de palabra en mayúscula
  y el resto en minúscula

  Args:
    breed: Nombre de raza a transformar

  Returns:
    str: Raza con las condiciones ya establecidas
  """

  breed_parts = re.split(r'\s+', breed)
  return ' '.join(part.capitalize() for part in breed_parts)

