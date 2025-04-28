from sqlalchemy import Column,String,Integer
from db import Base
from sqlalchemy.ext.declarative import declarative_base

class Ahc_old(Base):
    __tablename__="ahc_old"

    
    bis_id = Column(String)
    standardno = Column(String)
    str_ahc_name = Column(String)
    str_cml_no = Column(String)
    dt_validity_date = Column(String)
    address = Column(String)
    scope = Column(String)
    strnameowner = Column(String)
    strdesigowner = Column(String)
    stroffno = Column(String)
    stroffmail = Column(String)
    appstatus = Column(String)
    status = Column(String)
    appid = Column(String)
    regid = Column(String)
    ahc_latitude = Column(String)
    ahc_longitude = Column(String)
    lgd_state_id = Column(String)
    lgd_district_id = Column(String)
    lgd_district_name = Column(String)
    lgd_statename = Column(String)
    id = Column(Integer,primary_key=True)
  
