from fastapi import FastAPI, Depends
from db import get_db
from sqlalchemy.orm import Session
import uvicorn
from model import Ahc_old
from pydentic import User 


app = FastAPI()

fake_items_db = []

@app.get("/ahc_old")
async def ahc_old(db: Session= Depends(get_db)): 
    try:
        info = db.query(Ahc_old).all()
        return info  
    except Exception as e:
        print(f"Query error: {e}")
        return [] 
    
@app.post("/add_data")
async def create_item(item:User, db: Session = Depends(get_db)):
    
    data = Ahc_old(

    bis_id=item.bis_id,
    standardno=item.standardno,     
    str_ahc_name=item.str_ahc_name,
    str_cml_no=item.str_cml_no, 
    dt_validity_date=item.dt_validity_date,
    address=item.address,
    scope=item.scope,
    strnameowner=item.strnameowner,
    strdesigowner=item.strdesigowner,
    stroffno=item.stroffno,
    stroffmail=item.stroffmail,
    appstatus=item.appstatus,
    status=item.status,
    appid=item.appid,
    regid=item.regid,
    ahc_latitude=item.ahc_latitude,
    ahc_longitude=item.ahc_longitude,
    lgd_state_id=item.lgd_state_id,
    lgd_district_id=item.lgd_district_id,
    lgd_district_name=item.lgd_district_name,
    lgd_statename=item.lgd_statename,
    id=item.id
    )

    db.add(data)
    db.commit()
    db.refresh(data)
    return data

@app.put("/ahc_old/{id}")
async def update_item(id:int, db: Session= Depends(get_db)):
    data_add = db.query(Ahc_old).filter( Ahc_old.id == id).first()
    data_add.id = 1611
    data_add.standardno = "IS"
    db.commit()
    return {"message": "Standardno updated successfully"}

@app.delete("/ahc_old/{id}")
async def delete_item(id: int,db: Session= Depends(get_db)):
    data_add = db.query(Ahc_old).filter(Ahc_old.id == id).first()
    db.delete(data_add)
    db.commit()
    return {"message": "Item deleted successfully"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000
    )
    
