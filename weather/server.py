##########################################################################################
#    内蔵アプリケーションサーバーを起動します。
##########################################################################################
from flask import Flask
from flask_talisman import Talisman
import api.main as main

app = Flask(__name__)
Talisman(app)
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
)

@app.route("/check", methods=["GET", "POST"])
def index():
    return main.check()


if __name__ == "__main__":
    app.run(
        debug=False,
        host="0.0.0.0",
        port=8080
    )
