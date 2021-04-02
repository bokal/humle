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

bp = Blueprint("landing", __name__)


def get_apost(id):
    db = get_db()
    post = (
        db.execute(
            "SELECT p.id, title, body, created, author_id, username, img"
            " FROM post p JOIN user u ON p.author_id = u.id"
            " WHERE p.id = ?",
            (id,),
        )
        .fetchone()
    )

    if post is None:
        abort(404, f"Page id {id} doesn't exist.")

    return post

@bp.route("/")
def page():
    post = get_apost(2)
    return render_template("landing/index.html", post = post)
