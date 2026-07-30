from extensions import db
from datetime import datetime


class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    paid_by = db.Column(db.String(100), nullable=False)
    shipment_packages_id = db.Column(
        db.Integer,
        db.ForeignKey("shipment_packages.id"),
        nullable=False
    )
    currency = db.Column(db.String(10), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship
    shipment_package = db.relationship(
        "ShipmentPackage",
        back_populates="payments"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "paid_by": self.paid_by,
            "shipment_packages_id": self.shipment_packages_id,
            "currency": self.currency,
            "date": self.date.isoformat() if self.date else None,
        }