from marshmallow import fields

from config import ma


class UserPostSchema(ma.Schema):
    def __init__(self, **kwargs):
        super().__init__(strict=True, **kwargs)

    post_id = fields.Int()
    author_id = fields.Int()
    title = fields.Str()
    body = fields.Str()
    imageUrl = fields.Str()
    timestamp = fields.Str()


class UserSchema(ma.ModelSchema):
    user_id = fields.Int()
    login = fields.Str()
    password = fields.Str()
    timestamp = fields.DateTime()
    posts = fields.List(fields.Nested(UserPostSchema))
