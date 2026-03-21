import os

from flask import Flask

from web.routes import register_routes

STATIC_ASSET_VERSION = os.getenv("RENDER_GIT_COMMIT", "dev")


def create_app() -> Flask:
    app = Flask(__name__, static_folder="static", template_folder="templates", static_url_path="/static")
    app.config["STATIC_ASSET_VERSION"] = STATIC_ASSET_VERSION
    app.logger.info("Registering routes")
    register_routes(app)
    app.logger.info("Routes registered")
    return app


app = create_app()
app.logger.info("App instance created")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
