import os
from datetime import datetime
from config import db
from posts.models.post_model import Post
from posts.models.user_model import User

# Data to initialize database with
USERS = [
    {
        "login": "Tomas",
        "password": "Shelby",
        "posts": [
            ("newe", "be", "image", "2019-01-07 22:47:54"),
            ("qwe", "ert", "asd", "2019-01-07 22:47:54")
                ]
    }
]

# Delete database file if it exists currently
if os.path.exists("post.db"):
    os.remove("post.db")

# Create the database
db.create_all()

# iterate over the USERS structure and populate the database
for user in USERS:
    u = User(login=user.get("login"), password=user.get("password"))

    # Add the posts for the user
    for post in user.get("posts"):
        title, body, imageUrl, timestamp = post
        u.posts.append(
            Post(
                title=title,
                body=body,
                imageUrl=imageUrl,
                timestamp=datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
            )
        )
    db.session.add(u)

db.session.commit()

