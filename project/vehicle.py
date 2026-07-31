from app import db


class Vehicle(db.Model):
    __tablename__ = "vehicles"

    id = db.Column(db.Integer, primary_key=True)
    plate_number = db.Column(db.String(20), nullable=False, unique=True)
    status = db.Column(db.String(50), nullable=False)
    current_city_id = db.Column(
        db.Integer,
        db.ForeignKey("cities.id"),
        nullable=False
    )

    # Relationship
    current_city = db.relationship("City", back_populates="vehicles")

    # Shipments handled by this vehicle
    shipments = db.relationship(
        "Shipment",
        back_populates="vehicle",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Vehicle {self.plate_number}>"