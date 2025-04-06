from pydantic import BaseModel

class ClientDto(BaseModel):
  """
  Cliente usuario DTO

  Attributes:
    id (int): ID autogenerado de la DB para el usuario
    name (str): Nombre completo real del usuario, o nombre de la entidad veterinaria

  """

  id: int 
  name: str | None = None