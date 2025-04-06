
class EntityAlreadyExistsError(Exception):
  """
  Excepción lanzada debido a que ya existe una entidad ya existente en la base de datos
  """
  pass

class EntityNotFoundError(Exception):
  """
  Excepción lanzada por una entidad no encontrada en la base de datos
  """
  pass