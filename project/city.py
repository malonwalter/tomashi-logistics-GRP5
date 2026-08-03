CREATE TABLE cities (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country_id INTEGER,
    FOREIGN KEY(country_id)
        REFERENCES countries(id)
);
class City(db.Model):
    __tablename__ = "cities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    country_id = db.Column(
        db.Integer,
        db.ForeignKey("countries.id")
    )