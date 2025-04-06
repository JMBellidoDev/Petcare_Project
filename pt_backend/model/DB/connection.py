
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Local     -> SQLALCHEMY_DB_URL = 'postgresql://postgres:rootroot@localhost:5432/postgres'
#              SCHEMA = "petcare_db"
# Supabase  -> SQLALCHEMY_DB_URL = 'postgresql://postgres.tpzqgchlvgtrgtsfhpjy:SRcm8NA1vf3fZc1K@aws-0-eu-central-1.pooler.supabase.com:6543/postgres'
#              SCHEMA = "public"

SQLALCHEMY_DB_URL = 'postgresql://postgres:rootroot@localhost:5432/postgres'
SCHEMA = "petcare_db"

# Motor para las consultas
engine = create_engine(
  SQLALCHEMY_DB_URL, 
  echo = True, 
  execution_options = {"schema_translate_map": {None: SCHEMA}}
)

# Creación de clases SessionLocal y Base
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

