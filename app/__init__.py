"""ce fichier sert à configurer et initialiser l'application ainsi qu'à préparer 
l'intégration avec la base de données via la dépendance SQLAlchemy"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Importer et enregistrer le blueprint
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    with app.app_context():
        from . import routes
        db.create_all()

    return app
