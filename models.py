from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Define SQLite database
DATABASE_URL = "sqlite:///query_logs.db"

# Set up database engine and session
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define table schema
class QueryLog(Base):
    __tablename__ = "query_logs"

    id = Column(Integer, primary_key=True, index=True)
    case_type = Column(String, nullable=False)
    case_number = Column(String, nullable=False)
    year = Column(String, nullable=False)
    response = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Create table if not exists
Base.metadata.create_all(bind=engine)
