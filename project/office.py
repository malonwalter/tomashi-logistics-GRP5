from app import db


class Office(db.Model):
    __tablename__ = "offices"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    full_address = db.Column(db.String(255), nullable=False)

    city_id = db.Column(
        db.Integer,
        db.ForeignKey("cities.id"),
        nullable=False
    )

    # Relationship
    city = db.relationship("City", back_populates="offices")

    # Shipments
    origin_shipments = db.relationship(
        "Shipment",
        foreign_keys="Shipment.origin_office_id",
        back_populates="origin_office"
    )

    destination_shipments = db.relationship(
        "Shipment",
        foreign_keys="Shipment.destination_office_id",
        back_populates="destination_office"
    )

    def __repr__(self):
        return f"<Office {self.name}>"