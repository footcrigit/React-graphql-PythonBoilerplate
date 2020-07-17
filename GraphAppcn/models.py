from GraphAppcn import db,app
from sqlalchemy import Column, Integer,String,VARCHAR

class VehicleDetails(db.Model):
    __tablename__ = "VEHICLE_DETAILS"
    VEHICLE_TAG_NUM = Column(VARCHAR,primary_key = True)
    VEHICLE_MAKE = Column(VARCHAR)
    VEHICLE_MODEL = Column(VARCHAR)
