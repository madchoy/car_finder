from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, DECIMAL

Base = declarative_base()
class Car(Base):
    __tablename__ = 'car'
    id = Column(Integer, primary_key = True)
    year = Column(Integer)
    kilometers = Column(DECIMAL)
    selling_price = Column(DECIMAL)

engine = create_engine('sqlite:///car_finder.db')
Base.metadata.create_all(engine)
