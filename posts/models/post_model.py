from datetime import datetime
from config import db


class Post(db.Model):

    __tablename__ = "post"

    post_id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))
    title = db.Column(db.String(30), nullable=False)
    body = db.Column(db.String(150), nullable=False)
    imageUrl = db.Column(db.String)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow()
    )
#    likes = db.relationship(
#        "Like",
#        backref="user",
#        cascade="all, delete, delete-orphan",
#        single_parent=True,
#        order_by="desc(User.timestamp)"
#    )




