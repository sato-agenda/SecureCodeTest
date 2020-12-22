##########################################################################################
#    内蔵アプリケーションサーバーを起動します。
##########################################################################################
from flask import Flask, request
from flask_talisman import Talisman
import api.main as main

app = Flask(__name__)
app.config["SESSION_COOKIE_SECURE"] = True
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
Talisman(app)

@app.route("/is_holiday", methods=["GET", "POST"])
def index():
    return main.is_holiday(_get_request_json())


def _get_request_json():
    """GET/POST両方に対応した形式でリクエストデータを変換します。

    Returns:
        list: リクエストデータ
    """
    if request.method == "POST":
        return request.json
    else:
        return request.args


if __name__ == "__main__":
    app.run(
        debug=False,
        host="0.0.0.0",
        port=8080
    )
