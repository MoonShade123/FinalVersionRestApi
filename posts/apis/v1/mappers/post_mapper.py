from marshmallow import fields
from config import ma, db
from posts.models.post_model import Post


class PostSchema(ma.ModelSchema):
    def __init__(self, **kwargs):
        super().__init__(strict=True, **kwargs)

        class Meta:
            model = Post
            sqla_session = db.session

        users = fields.Nested("PostUserSchema", default=None)


class PostUserSchema(ma.ModelSchema):
    def __init__(self, **kwargs):
        super().__init__(strict=True, **kwargs)

        user_id = fields.Int()
        login = fields.Str()
        password = fields.Str()
        timestamp = fields.DateTime()
