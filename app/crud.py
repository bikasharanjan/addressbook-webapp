import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from . import models, schemas

logger = logging.getLogger(__name__)

def create_address(db: Session, addr: schemas.AddressCreate):
    try:
        logger.info(f"Creating address: {addr.name}")
        db_addr = models.Address(**addr.dict())
        db.add(db_addr)
        db.commit()
        db.refresh(db_addr)
        logger.info(f"Address created with ID: {db_addr.id}")
        return db_addr
    except SQLAlchemyError as e:
        logger.exception("Database error while creating address")
        db.rollback()
        raise e

def get_address(db: Session, address_id: int):
    try:
        logger.info(f"Fetching address with ID: {address_id}")
        return db.query(models.Address).filter(models.Address.id == address_id).first()
    except SQLAlchemyError as e:
        logger.exception(f"Database error while fetching address ID: {address_id}")
        raise e

def get_addresses(db: Session, skip: int = 0, limit: int = 10):
    try:
        logger.info(f"Fetching all addresses with skip={skip}, limit={limit}")
        return db.query(models.Address).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        logger.exception("Database error while fetching all addresses")
        raise e

def update_address(db: Session, address_id: int, addr_update: schemas.AddressUpdate):
    try:
        logger.info(f"Updating address with ID: {address_id}")
        db_addr = get_address(db, address_id)
        if not db_addr:
            logger.warning(f"Address with ID {address_id} not found for update")
            return None
        for key, value in addr_update.dict(exclude_unset=True).items():
            setattr(db_addr, key, value)
        db.commit()
        db.refresh(db_addr)
        logger.info(f"Address with ID {address_id} updated")
        return db_addr
    except SQLAlchemyError as e:
        logger.exception(f"Database error while updating address ID: {address_id}")
        db.rollback()
        raise e

def delete_address(db: Session, address_id: int):
    try:
        logger.info(f"Deleting address with ID: {address_id}")
        db_addr = get_address(db, address_id)
        if not db_addr:
            logger.warning(f"Address with ID {address_id} not found for deletion")
            return None
        db.delete(db_addr)
        db.commit()
        logger.info(f"Address with ID {address_id} deleted")
        return db_addr
    except SQLAlchemyError as e:
        logger.exception(f"Database error while deleting address ID: {address_id}")
        db.rollback()
        raise e
