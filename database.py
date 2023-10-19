from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///todooo.db")
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
