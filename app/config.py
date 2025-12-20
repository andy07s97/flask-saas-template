# app/config.py
import os

def load_config(app):
    # Project paths
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))
    INSTANCE_DIR = os.path.join(PROJECT_ROOT, "instance")

    # Ensure instance folder exists
    os.makedirs(INSTANCE_DIR, exist_ok=True)

    # Security
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-change-me")

    # Database (absolute path, production-safe)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{os.path.join(INSTANCE_DIR, 'app.db')}"
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
