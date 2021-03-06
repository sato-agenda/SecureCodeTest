##########################################################################################
#    各種APIに接続するプロキシーサーバーを起動します。
##########################################################################################
from flask import Flask, request
from flask_cors import CORS
from flask_talisman import Talisman
import requests

# 定数定義
SERVICE_PORT = 8080

app = Flask(__name__)
app.config["SESSION_COOKIE_SECURE"] = True
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["PREFERRED_URL_SCHEME"] = "https"
CORS(app)
Talisman(app)


@app.route("/<category>/<method>", methods=["GET", "POST"])
def proxy(category: str, method: str):
    return requests.post(f"http://{category}:{SERVICE_PORT}/{method}",
        headers={"Content-Type": "application/json"},
        json=_get_request_json()
    ).text


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
