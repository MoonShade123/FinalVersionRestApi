from marshmallow import fields
from config import ma
from posts.apis.v1.mappers.user_mapper import UserSchema


class PostUserSchema(ma.Schema):
    def __init__(self, **kwargs):
        super().__init__(strict=True, **kwargs)

        user_id = fields.Int()


class PostSchema(ma.Schema):
    post_id = fields.Int()
    author_id = fields.List(fields.Nested(PostUserSchema))
    title = fields.Str()
    body = fields.Str()
    imageUrl = fields.Str()
    timestamp = fields.DateTime()
