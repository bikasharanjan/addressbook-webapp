from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas, utils
from app.database import SessionLocal

router = APIRouter(prefix="/addresses", tags=["addresses"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.AddressOut)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    return crud.create_address(db, address)

@router.get("/", response_model=List[schemas.AddressOut])
def read_addresses(db: Session = Depends(get_db)):
    return crud.get_addresses(db)

@router.get("/within", response_model=List[schemas.AddressOut])
def read_addresses_within(lat: float, lon: float, dist_km: float, db: Session = Depends(get_db)):
    results = []
    for a in crud.get_addresses(db):
        if utils.haversine(lat, lon, a.latitude, a.longitude) <= dist_km:
            results.append(a)
    return results

@router.put("/{address_id}", response_model=schemas.AddressOut)
def update_address(address_id: int, address: schemas.AddressUpdate, db: Session = Depends(get_db)):
    updated = crud.update_address(db, address_id, address)
    if not updated:
        raise HTTPException(status_code=404, detail="Address not found")
    return updated

@router.delete("/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_address(db, address_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Address not found")
    return {"detail": "Address deleted"}
