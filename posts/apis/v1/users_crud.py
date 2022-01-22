from flask import make_response, abort
from config import db, connex_app
from posts.models.post_model import Post
from posts.models.user_model import User
from posts.apis.v1.mappers.user_mapper import UserSchema


@connex_app.route('/api/users', methods=['GET'])
def read_all():
    users = User.query.order_by(User.user_id).all()
    user_schema = UserSchema(many=True)
    data = user_schema.dumps(users).data
    return data


@connex_app.route('/api/users/<int:user_id>', methods=['GET'])
def read_one(user_id):
    user = (
        User.query.filter(User.user_id == user_id)
        .outerjoin(Post)
        .one_or_none()
    )
    if user is not None:
        user_schema = UserSchema()
        data = user_schema.dumps(user).data
        return data
    else:
        abort(404, f"User with Id: {user_id} not found...")


@connex_app.route('/api/users', methods=['POST'])
def create(user):
    login = user.get("login")
    password = user.get("password")
    already_existing = (
        User.query.filter(User.login == login)
        .one_or_none()
    )
    if already_existing is None:
        user_schema = UserSchema()
        new_user = user_schema.load(user, session=db.session).data
        db.session.add(new_user)
        db.session.commit()
        data = user_schema.dump(new_user).data
        return data, 201
    else:
        abort(409, f"User with this login: {login} already exists...")


def update(user_id, user):
    update_user = User.query.filter(
        User.user_id == user_id
    ).one_or_none()
    if update_user is not None:
        update_schema = UserSchema()
        updated = update_schema.load(user, session=db.session).data
        updated.user_id = update_user.user_id
        db.session.merge(updated)
        db.session.commit()
        data = update_schema.dump(update_user).data
        return data, 200
    else:
        abort(404, f"User not found with Id: {user_id}...")


def delete(user_id):
    user = User.query.filter(User.user_id == user_id).one_or_none()
    if user is not None:
        db.session.delete(user)
        db.session.commit()
        return make_response(f"User with Id:{user_id} successfully deleted...", 200)
    else:
        abort(404, f"User with Id: {user_id} doesn't exists...")