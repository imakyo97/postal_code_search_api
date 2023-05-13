from flask import Flask
from flask import jsonify
from flask import request

from postal_code_db import postal_code_repository


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route('/')
def hello_postal_code_search_api():
    return '郵便番号APIです。'

@app.route('/address', methods=['GET'])
def get_address():
    repo = postal_code_repository.PostalCodeRepository()
    code = request.args.get('code')
    address = repo.fetch_address(code)
    if address:
        json = {
            "address": address
        }
        return jsonify(json)
    else:
        json = {
            "error": "該当する住所がありませんでした"
        }
        return jsonify(json), 404

def main():
    app.debug = True
    app.run()

if __name__ == '__main__':
    main()
