from flask import Flask

from app.root import root

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

app.register_blueprint(root)
