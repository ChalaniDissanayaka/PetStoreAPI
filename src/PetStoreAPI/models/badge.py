from ..init import db


class BadgeModel(db.Model):
    __tablename__ = "badges"

    id = db.Column(db.Integer, primary_key=True)
    badge_name = db.Column(db.String(80), unique=True, nullable=False)
    colour_code = db.Column(db.String(20), unique=False, nullable=False)
    discount = db.Column(db.Float(precision=2), unique=False, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)

    store = db.relationship("StoreModel", back_populates="badges")
