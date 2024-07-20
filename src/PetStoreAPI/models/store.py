from ..init import db


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(80), unique=True, nullable=False)
    store_location = db.Column(db.String(100), unique=True, nullable=False)

    petitems = db.relationship("PetItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")
