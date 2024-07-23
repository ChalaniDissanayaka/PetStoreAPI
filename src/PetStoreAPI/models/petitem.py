from ..init import db


class PetItemModel(db.Model):
    __tablename__ = "petitems"

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(80), unique=True, nullable=False)
    item_description = db.Column(db.String(100))
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False)

    store = db.relationship("StoreModel", back_populates="petitems")
    badges = db.relationship("BadgeModel", back_populates="petitems", secondary="petitems_badges")
