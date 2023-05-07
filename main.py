from flask import Flask
from flask import request

from postal_code_db import postal_code_repository


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

postal_code_repository = postal_code_repository.PostalCodeRepository()


@app.route('/')
def hello_postal_code_search_api():
    return '郵便番号APIです。'

@app.route('/address', methods=['GET'])
def get_address():
    code = request.args.get('code')
    if code is None:
        return {
            "error": "パラメータが不正"
        }, 400
    address = postal_code_repository.fetch_address(code)
    if address is None:
        return {
            "error": "該当する住所がありませんでした"
        }, 400
    return {
        "address": address,
    }, 200

def main():
    app.debug = True
    app.run()

if __name__ == '__main__':
    main()
