from extensions import db
from datetime import datetime


class ShipmentPackage(db.Model):
    __tablename__ = "shipment_packages"

    id = db.Column(db.Integer, primary_key=True)
    shipment_id = db.Column(
        db.Integer,
        db.ForeignKey("shipments.id"),
        nullable=False
    )
    package_id = db.Column(
        db.Integer,
        db.ForeignKey("packages.id"),
        nullable=False
    )
    loaded_at = db.Column(db.DateTime, default=datetime.utcnow)
    loaded_location = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))
    shipment_cost = db.Column(db.Float, nullable=False)

    # Relationships
    shipment = db.relationship(
        "Shipment",
        back_populates="shipment_packages"
    )

    package = db.relationship(
        "Package",
        back_populates="shipment_packages"
    )

    payments = db.relationship(
        "Payment",
        back_populates="shipment_package",
        cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "shipment_id": self.shipment_id,
            "package_id": self.package_id,
            "loaded_at": self.loaded_at.isoformat() if self.loaded_at else None,
            "loaded_location": self.loaded_location,
            "description": self.description,
            "shipment_cost": self.shipment_cost,
        }