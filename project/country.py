CREATE TABLE countries (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
class Country(db.Model):
    __tablename__ = "countries"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

cities = db.relationship(
    "City",
    backref="country",
    lazy=True
)    