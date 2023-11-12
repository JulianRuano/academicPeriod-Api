from config.database import Base
from sqlalchemy import Column, Integer, String

class Period(Base):
    __tablename__ = 'periods'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    year = Column(String)
    semester = Column(Integer)
    startDate = Column(String)
    endDate = Column(String)


    


   