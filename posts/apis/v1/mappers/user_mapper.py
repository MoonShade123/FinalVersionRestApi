from marshmallow import fields

from config import ma, db
from posts.models.user_model import User


class UserSchema(ma.ModelSchema):
    def __init__(self, **kwargs):
        super().__init__(strict=True, **kwargs)

    class Meta:
        model = User
        sqla_session = db.session

    posts = fields.Nested("UserPostSchema", default=[], many=True)


class UserPostSchema(ma.ModelSchema):
    def __init__(self, **kwargs):
        super().__init__(strict=True, **kwargs)

    post_id = fields.Int()
    author_id = fields.Int()
    title = fields.Str()
    body = fields.Str()
    imageUrl = fields.Str()
    timestamp = fields.Str()

