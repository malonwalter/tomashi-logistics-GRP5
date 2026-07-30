
from datetime import datetime
from extensions import db





class Shipments(db.Model):
    __tablename__ = "shipments"

    id = db.Column( db.Integer , primary_key= True)
    departure_date = db.Column(db.DateTime , nullable= False)
    shipment_status = db.Column(db.String(50), nullable= False) 
    expected_arrival = db.Column(db.DateTime , nullable=False)
    actual_arrival = db.Column(db.DateTime , nullable=False)
    distance_in_km = db.Column(db.Float , nullable=False)

    vehicle_id = db.Column(db.Integer , db.ForeignKey("vehicles.id"), nullable= False )
    origin_office_id = db.Column(db.Integer , db.ForeignKey("offices.id"), nullable=False)
    destination_office_id = db.Column(db.Integer , db.ForeignKey("offices.id"), nullable=False)
    vehicle = db.relationship("Vehicle" , backref="shipments")
    origin_office = db.relationship("Offices" , foreign_keys = [origin_office_id])
    destination_office = db.relationship("Offices" , foreign_keys=[destination_office_id])
    


class Packages(db.Model):
    __tablename__ = "packages"

    id = db.Column(db.Integer , primary_key = True)
    claim_number = db.Column(db.String(50), nullable=False , unique=True)
    status = db.Column(db.String(50) , nullable=False)
    description = db.Column(db.String(50) , nullable=False)
    weight = db.Column(db.Float , nullable=False)

    supplier_id = db.Column(db.Integer , db.ForeignKey("suppliers.id"), nullable=False )
    supplier = db.relationship("Supplier" , backref="packages")