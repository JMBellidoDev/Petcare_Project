from model.entity.user import UserCreate

class VetEntity(UserCreate):
  """
  Entidad veterinaria, la cual será capaz de administrar cualquier dato de la aplicación relacionada con clientes
  y mascotas. Además, será la encargada de gestionar el acceso a los distintos veterinarios a la aplicación, tanto
  su acceso como su consecuente baja
  """

  cif: str | None = None
  name: str | None = None
  address: str | None = None
  phone_number: str | None = None