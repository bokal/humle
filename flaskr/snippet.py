from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

def get_snippet(title):
    db = get_db()
    snippet = (
        db.execute(
            "SELECT p.id, title, body, created, author_id, username, img"
            " FROM post p JOIN user u ON p.author_id = u.id"
            " WHERE p.title = ? and typ='snippet'",
            (title,),
        )
        .fetchone()
    )

    if snippet is None:
        snippet = {'id':0,'body':''}

    return snippet

