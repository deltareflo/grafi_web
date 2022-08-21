from shared import db
from auth.model import Usuarios
from flask_login import LoginManager
from flask import Flask
from config import DeveloperConfig
from decorators import admin_required

app = Flask(__name__)
app.config.from_object(DeveloperConfig)
login_manager = LoginManager(app)
login_manager.login_view = "auth.login"
db.app = app
db.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return Usuarios.get_by_id(int(user_id))

# Blueprints
from auth import auth_bp
app.register_blueprint(auth_bp)

from public import public_bp
app.register_blueprint(public_bp)

if __name__ == '__main__':

    db.create_all()
    app.run(debug=True)
