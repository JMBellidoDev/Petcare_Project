from typing import Annotated, Optional, List
from sqlalchemy import Boolean, Integer, String, ForeignKey, Date, DateTime, Table, LargeBinary, Column
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship

from model.DB.connection import engine

# Clase Base para definir entidades
class Base(DeclarativeBase):
  pass


# -----------------------------------------------------------------------------
# Keys predefinidas
# -----------------------------------------------------------------------------

int_pk = Annotated[int, mapped_column(Integer, primary_key = True, autoincrement=True)]

app_user_pk_fk = Annotated[int, mapped_column(Integer, ForeignKey("app_user.id"), primary_key=True)]
vet_entity_fk = Annotated[int, mapped_column(Integer, ForeignKey("vet_entity.id"))]
pet_fk = Annotated[int, mapped_column(Integer, ForeignKey("pet.id"))]
vet_fk = Annotated[int, mapped_column(Integer, ForeignKey("vet.id"))]
client_fk = Annotated[int, mapped_column(Integer, ForeignKey("client.id"))]



# -----------------------------------------------------------------------------
# Clase User
# -----------------------------------------------------------------------------

class User(Base):
  """
  Construcción de un usuario base de la aplicación en base a los campos de la DB

  Attributes:
    __tablename__ (str): Indica el nombre de la tabla asociada al usuario en la DB

    id (int): ID generado por la base de datos de forma auto incremental
    username (str): Nombre del usuario
    hashed_password (str): Contraseña ya hasheada asociada al usuario
    email (str): Email asociado al usuario
    enabled (bool): Indica si el usuario está activo o no
    role (str): Role que posee el usuario. Será 'client', 'vet' o 'vet_entity'
  """

  __tablename__ = "app_user"

  id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
  username: Mapped[str] = mapped_column(String, unique=True, index=True)
  hashed_password: Mapped[str] = mapped_column(String)
  email: Mapped[str] = mapped_column(String, unique=True, index=True)
  enabled: Mapped[bool] = mapped_column(Boolean, default=True)
  role: Mapped[str] = mapped_column(String)

  client: Mapped["Client"] = relationship('Client', back_populates='user')
  vet: Mapped["Vet"] = relationship('Vet', back_populates='user')
  vet_entity: Mapped["VetEntity"] = relationship('VetEntity', back_populates='user')


# Tabla intermedia entre cliente y mascota
client_pet_table = Table(
  "client_pets",
  Base.metadata,
  Column("pet_id", ForeignKey("pet.id")),
  Column("client_id", ForeignKey("client.id")),
  Column("show", Boolean, default = True)
)

class Client(User):
  """
  Construcción de un usuario base de la aplicación en base a los campos de la DB

  Attributes:
    __tablename__ (str): Indica el nombre de la tabla asociada al usuario en la DB

    id (int): ID de usuario
    national_id_document (str): Documento nacional de identidad (NIF/NIE)
    name (str): Nombre completo real del usuario
    birthdate (date): Fecha de nacimiento
    address (str): Dirección de residencia del usuario
    phone_number (str): Número de teléfono del usuario
  """

  __tablename__ = "client"


  id: Mapped[app_user_pk_fk] 
  national_id_document: Mapped[str] = mapped_column(String, unique=True, index=True)
  name: Mapped[str] = mapped_column(String)
  birthdate: Mapped[Date] = mapped_column(Date)
  address: Mapped[str] = mapped_column(String)
  phone_number: Mapped[str] = mapped_column(String, unique=True, index=True)

  user: Mapped["User"] = relationship("User", back_populates="client")
  pets: Mapped[list["Pet"]] = relationship("Pet", secondary=client_pet_table, back_populates="clients")
  appointments: Mapped[list["Appointment"]] = relationship("Appointment", back_populates="client")


class Vet(User):
  """
  Construcción de un veterinario de la aplicación en base a los campos de la DB

  Attributes:
    __tablename__ (str): Indica el nombre de la tabla asociada al usuario en la DB

    id (int): ID de usuario
    national_id_document (str): Documento nacional de identidad (NIF/NIE)
    name (str): Nombre completo real del usuario
    registration_number (str): Número de registro (Número de colegiado)
    vet_entity_id (int): ID de la entidad veterinaria que tiene registrado al veterinario
    """
  
  __tablename__ = "vet"


  id: Mapped[app_user_pk_fk] 
  national_id_document: Mapped[str] = mapped_column(String, unique=True, index=True)
  name: Mapped[str] = mapped_column(String)
  registration_number: Mapped[str] = mapped_column(String, unique=True)
  vet_entity_id: Mapped[vet_entity_fk]

  user: Mapped["User"] = relationship("User", back_populates="vet")
  vet_entity: Mapped["VetEntity"] = relationship("VetEntity", back_populates="vets", foreign_keys=lambda: [Vet.vet_entity_id])
  appointments: Mapped[list["Appointment"]] = relationship("Appointment", back_populates="vet")
  reports: Mapped[list["Report"]] = relationship("Report", back_populates="vet")


class VetEntity(User):
  """
  Construcción de una entidad veterinaria de la aplicación en base a los campos de la DB

  Attributes:
    __tablename__ (str): Indica el nombre de la tabla asociada al usuario en la DB

    id (int): ID de usuario
    name (str): Nombre completo real del usuario
    cif (str): CIF de la empresa
    address (str): Dirección física donde se encuentra
    phone_number (str): Número de teléfono asociado a la entidad veterinaria
    """
  
  __tablename__ = "vet_entity"


  id: Mapped[app_user_pk_fk]
  name: Mapped[str] = mapped_column(String)
  cif: Mapped[str] = mapped_column(String, unique=True, index=True)
  address: Mapped[str] = mapped_column(String, unique=True)
  phone_number: Mapped[str] = mapped_column(String)

  user: Mapped["User"] = relationship("User", back_populates="vet_entity")
  vets: Mapped[list["Vet"]] = relationship("Vet", back_populates="vet_entity", foreign_keys=lambda: [Vet.vet_entity_id])

class Pet(Base):
  """
  Construcción de una mascota de la aplicación en base a los campos de la DB

  Attributes:
    __tablename__ (str): Indica el nombre de la tabla asociada al usuario en la DB

    id (int): ID de la mascota
    chip_number (str): Número del chip de la mascota
    type (str): Tipo de mascota. Será dog, cat, ferret, bird, rabbit, horse
    breed (str): Dirección física donde se encuentra
    name (str): Número de teléfono asociado a la entidad veterinaria
    birthdate (date): Número de teléfono asociado a la entidad veterinaria
    alive (bool): Número de teléfono asociado a la entidad veterinaria
    castrated (bool): Número de teléfono asociado a la entidad veterinaria
    image (LargeBinary)
    """
  
  __tablename__ = "pet"

  id: Mapped[int_pk]
  chip_number: Mapped[str] = mapped_column(String, unique=True, index=True)
  type: Mapped[str] = mapped_column(String)
  breed: Mapped[str] = mapped_column(String)
  name: Mapped[str] = mapped_column(String)
  birthdate: Mapped[Date] = mapped_column(Date)
  alive: Mapped[bool] = mapped_column(Boolean)
  castrated: Mapped[bool] = mapped_column(Boolean)
  image: Mapped[bytes] = mapped_column(LargeBinary)

  clients: Mapped[list["Client"]] = relationship("Client", secondary=client_pet_table, back_populates="pets")
  appointments: Mapped[list["Appointment"]] = relationship("Appointment", back_populates="pet")
  reports: Mapped[list["Report"]] = relationship("Report", back_populates="pet")


class Appointment(Base):
  """
  Construcción de una cita de la aplicación en base a los campos de la DB. Constituirá una cita
  entre la mascota y el veterinario, además de incluir un usuario que se encargue de llevar a la
  mascota

  Attributes:
    __tablename__ (str): Indica el nombre de la tabla asociada al usuario en la DB

    id (int): ID de la cita
    pet_id (int): ID de la mascota
    vet_id (int): ID del veterinario que atenderá a dicha mascota
    client_id (int): ID del cliente que acompañará a la mascota a la cita
    appointment_date (datetime): Fecha y hora en la cual se produce la cita
  """
  
  __tablename__ = "appointment"

  id: Mapped[int_pk]
  pet_id: Mapped[pet_fk]
  vet_id: Mapped[vet_fk]
  client_id: Mapped[client_fk]
  appointment_date: Mapped[DateTime] = mapped_column(DateTime)

  vet: Mapped["Vet"] = relationship("Vet", back_populates="appointments")
  pet: Mapped["Pet"] = relationship("Pet", back_populates="appointments")
  client: Mapped["Client"] = relationship("Client", back_populates="appointments")

class Report(Base):
  """
  Construcción de un informe veterinario 

  Attributes:
    __tablename__ (str): Indica el nombre de la tabla asociada al usuario en la DB
    pet_id (int): ID de la mascota
    vet_id (int): ID del veterinario que atendió a dicha mascota y realizó el informe
    reason (str): Razón por la cual se produce el informe
    diagnosis (str): Diagnóstico clínico del veterinario
    treatment (str): Tratamiento a seguir por la mascota
    report_date
  """

  __tablename__ = "report"

  id: Mapped[int_pk]
  pet_id: Mapped[pet_fk]
  vet_id: Mapped[vet_fk]
  reason: Mapped[str] = mapped_column(String)
  diagnosis: Mapped[str] = mapped_column(String)
  treatment: Mapped[str] = mapped_column(String)
  report_date: Mapped[DateTime] = mapped_column(DateTime)

  pet: Mapped["Pet"] = relationship("Pet", back_populates="reports")
  vet: Mapped["Vet"] = relationship("Vet", back_populates="reports")

Base.metadata.create_all(engine)