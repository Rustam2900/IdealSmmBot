# from sqlalchemy import create_engine, Column, Integer, VARCHAR, String, BigInteger
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# engine = create_engine('postgresql://postgres:rus_2900@localhost/SMM', echo=True)
# Base = declarative_base()
# Session = sessionmaker(bind=engine)
#
#
# class SMM(Base):
#     __tablename__ = 'users_table'
#
#     id = Column(Integer, primary_key=True)
#     user_id = Column(BigInteger, unique=True)
#     first_name = Column(String)
#     lang = Column(VARCHAR(3))
#
#
# Base.metadata.create_all(engine)
