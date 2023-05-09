from flask import Blueprint
from views import views

views = Blueprint("views")
app.register_blueprint(views, url_prefix="/")

@views.route("/")
def home():
    return "home page"