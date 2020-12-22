##########################################################################################
#    内蔵アプリケーションサーバーを起動します。
##########################################################################################
from flask import Flask
from flask_tailsman import Tailsman
import api.main as main

app = Flask(__name__)
Tailsman(app)

@app.route("/check", methods=["GET", "POST"])
def index():
    return main.check()


if __name__ == "__main__":
    app.run(
        debug=False,
        host="0.0.0.0",
        port=8080
    )
