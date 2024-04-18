from sqlalchemy import create_engine, Column, Integer, String, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:rus_2900@localhost/SmmBot", echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)


# class Ramadan(Base):
#     __tablename__ = 'bot'
#     id = Column(Integer, primary_key=True, unique=True)
#     user_id = Column(BigInteger)
#     username = Column(String)
#     first_name = Column(String)
#     created = Column(DateTime)


Base.metadata.create_all(engine)
