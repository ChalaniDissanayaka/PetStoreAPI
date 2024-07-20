from marshmallow import Schema, fields


class PlainPetItemSchema(Schema):
    id = fields.Str(dump_only=True)
    item_name = fields.Str(required=True)
    item_description = fields.Str()
    price = fields.Float(required=True)


class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    store_name = fields.Str(required=True)
    store_location = fields.Str(required=True)


class PetItemUpdateSchema(Schema):
    item_name = fields.Str()
    item_description = fields.Str()
    price = fields.Float()
    store_id = fields.Int()


class PetItemSchema(PlainPetItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)


class StoreSchema(PlainStoreSchema):
    petitems = fields.List(fields.Nested(PlainPetItemSchema()), dump_only=True)
