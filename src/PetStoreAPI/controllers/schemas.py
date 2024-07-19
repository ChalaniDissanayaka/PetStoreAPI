from marshmallow import Schema, fields


class PetItemSchema(Schema):
    id = fields.Str(dump_only=True)
    item_name = fields.Str(required=True)
    item_description = fields.Str()
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)


class PetItemUpdateSchema(Schema):
    item_name = fields.Str()
    item_description = fields.Str()
    price = fields.Float()


class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    store_name = fields.Str(required=True)
    store_location = fields.Str(required=True)
