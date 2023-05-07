from flask import Flask
from flask import request


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route('/')
def hello_postal_code_search_api():
    return '郵便番号APIです。'

@app.route('/address', methods=['GET'])
def get_address():
    code = request.args.get('code')
    if code is None:
        return {
            "error": "リクエストが不正"
        }, 400
    return {
        "address": code,
    }, 200

def main():
    app.debug = True
    app.run()

if __name__ == '__main__':
    main()
