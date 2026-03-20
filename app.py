from flask import Flask

from web.routes import register_routes

STATIC_ASSET_VERSION = "20260320b"


def create_app() -> Flask:
    app = Flask(__name__, static_folder="static", template_folder="templates", static_url_path="/static")
    app.config["STATIC_ASSET_VERSION"] = STATIC_ASSET_VERSION
    register_routes(app)
    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
