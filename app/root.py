from flask import Blueprint
from flask import jsonify
from flask import request

from app.postal_code_db import postal_code_repository


root = Blueprint('root', __name__, url_prefix='/')


@root.route('/')
def hello_postal_code_search_api():
    return '郵便番号APIです。'


@root.route("/address", methods=["GET"])
def get_address():
    repo = postal_code_repository.PostalCodeRepository()
    code = request.args.get("code")
    fetch_address = repo.fetch_address(code)
    if fetch_address:
        json = {"address": fetch_address}
        return jsonify(json)
    else:
        json = {"error": "該当する住所がありませんでした"}
        return jsonify(json), 404
