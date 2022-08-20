from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import column, String, Integer, ForeignKey, Boolean, Text, Date, func
from models import TimestampMixin


class Usuarios(db.Model, UserMixin):
    __tablename__= 'grafi_usuarios'

    id = db.Column(Integer, primary_key=True)
    nombre= db.Column(String(length=50), nullable=False)
    email = db.Column(String(length=150), unique=True)
    telefono = db.Column(Integer)
    password= db.Column(String(length=128))
    is_admin = db.Column(db.Boolean, default=False)
    # Foreignkey
    id_rol = db.Column(Integer, ForeignKey('rol_usuarios.id'))
    rol = db.relationship('Roles', backref='rol_user', lazy=True)

    def __repr__(self):
        return f'<User {self.email}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Usuarios.query.get(id)
    @staticmethod
    def get_by_email(email):
        return Usuarios.query.filter_by(email=email).first()


class Roles(db.Model, TimestampMixin):
    __tablename__ = 'rol_usuarios'
    id = db.Column(Integer, primary_key=True)
    nombre = db.Column(String(length=30), nullable=False)
    descripcion = db.Column(String(length=100))
