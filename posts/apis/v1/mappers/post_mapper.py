from marshmallow import fields
from config import ma, db
from posts.models.post_model import Post


class PostSchema(ma.ModelSchema):
    def __init__(self, **kwargs):
        super().__init__(strict=True, **kwargs)

    class Meta:
        model = Post
        sqla_session = db.session

    author_id = fields.Nested("PostUserSchema", default=[])
    liked = fields.Nested("PostLikeSchema", default=[], many=True)


class PostUserSchema(ma.ModelSchema):
    user_id = fields.Int()


class PostLikeSchema(ma.ModelSchema):
    like_id = fields.Int()
    user_id = fields.Int()
    post_id = fields.Int()

