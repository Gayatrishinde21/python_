from pydantic import BaseModel


class User(BaseModel):
    
    bis_id : str
    standardno : str
    str_ahc_name : str
    str_cml_no : str
    dt_validity_date : str
    address :str
    scope : str
    strnameowner : str
    strdesigowner : str
    stroffno : str
    stroffmail : str
    appstatus : str
    status :str
    appid :str
    regid :str
    ahc_latitude :str
    ahc_longitude :str
    lgd_state_id :str
    lgd_district_id :str
    lgd_district_name :str
    lgd_statename : str
    id : int 

     
