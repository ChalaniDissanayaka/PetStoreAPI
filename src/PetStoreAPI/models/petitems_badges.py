from ..init import db


class PetItemBadgeModel(db.Model):
    __tablename__ = "petitems_badges"

    id = db.Column(db.Integer, primary_key=True)
    petitem_id = db.Column(db.Integer, db.ForeignKey("petitems.id"))
    badge_id = db.Column(db.Integer, db.ForeignKey("badges.id"))
