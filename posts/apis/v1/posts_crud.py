from flask import make_response, abort, request
from config import db, connex_app
from posts.models.post_model import Post
from posts.models.user_model import User
from posts.apis.v1.mappers.post_mapper import PostSchema


@connex_app.route('/api/users/posts', methods=['GET'])
def read_all_posts():
    posts = Post.query.order_by(db.desc(Post.post_id)).all()
    post_schema = PostSchema(many=True, exclude=['user.posts'])
    data = post_schema.dumps(posts).data
    return data


@connex_app.route('/api/users/<int:user_id>/posts/<int:post_id>', methods=["GET"])
def read_post_by_id(user_id, post_id):
    post = (
        Post.query.join(User, User.user_id == Post.author_id)
        .filter(User.user_id == user_id)
        .filter(Post.post_id == post_id)
        .one_or_none()
    )
    if post is not None:
        post_schema = PostSchema()
        data = post_schema.dumps(post).data
        return data
    else:
        abort(404, f"Post with Id:{post_id} is not found...")


@connex_app.route('/api/users/<int:user_id>/posts', methods=['POST'])
def create_post(user_id):
    post = request.get_json(force=True)
    title = post.get('title')
    body = post.get('body')
    imageUrl = post.get('imageUrl')

    user = User.query.filter(User.user_id == user_id).one_or_none()
    if user is None:
        abort(404, f"User with Id:{user_id}, is not found...")

    create_schema = PostSchema()
    new_post = create_schema.load(post, session=db.session).data
    user.posts.append(new_post)
    db.session.commit()
    data = create_schema.dumps(new_post).data
    return data, 201


@connex_app.route('/api/users/<int:user_id>/posts/<int:post_id>', methods=['PUT'])
def update_post(user_id, post_id):
    post = request.get_json(force=True)





