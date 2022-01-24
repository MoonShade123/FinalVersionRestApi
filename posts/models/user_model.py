from datetime import datetime
from config import db


class User(db.Model):

    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(15))
    password = db.Column(db.String(30))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    posts = db.relationship(
        "Post",
        backref="user",
        cascade="all, delete, delete-orphan",
        single_parent=True,
        order_by="desc(Post.post_id)"
    )

