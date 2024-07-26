from marshmallow import Schema, fields


class PlainPetItemSchema(Schema):
    id = fields.Int(dump_only=True)
    item_name = fields.Str(required=True)
    item_description = fields.Str()
    price = fields.Float(required=True)


class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    store_name = fields.Str(required=True)
    store_location = fields.Str(required=True)


class PlainBadgeSchema(Schema):
    id = fields.Int(dump_only=True)
    badge_name = fields.Str()
    colour_code = fields.Str()
    discount = fields.Float()


class PetItemUpdateSchema(Schema):
    item_name = fields.Str()
    item_description = fields.Str()
    price = fields.Float()
    store_id = fields.Int()


class PetItemSchema(PlainPetItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    badges = fields.List(fields.Nested(PlainBadgeSchema()), dump_only=True)


class StoreSchema(PlainStoreSchema):
    petitems = fields.List(fields.Nested(PlainPetItemSchema()), dump_only=True)
    badges = fields.List(fields.Nested(PlainBadgeSchema()), dump_only=True)


class BadgeSchema(PlainBadgeSchema):
    store_id = fields.Int(load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    petitems = fields.List(fields.Nested(PlainPetItemSchema()), dump_only=True)


class BadgeAndPetItemSchema(Schema):
    message = fields.Str()
    petitem = fields.Nested(PetItemSchema)
    badge = fields.Nested(BadgeSchema)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)


class UserUpdateSchema(Schema):
    username = fields.Str()
    password = fields.Str()
