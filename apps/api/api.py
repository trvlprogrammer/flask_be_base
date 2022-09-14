from apps.api import bp
from flask import jsonify, request, current_app
from apps import api_response

@bp.route("/home", methods=["GET"])
def home():

    return api_response("success","Success for the first endpoint", "Welcome!")