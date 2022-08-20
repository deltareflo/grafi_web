from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, BooleanField, TextAreaField,\
    DateTimeField, SelectField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=50)])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    telefono = IntegerField('Telefono', render_kw={"placeholder": "0971553022"})
    email = StringField('Email', validators=[DataRequired(), Email()])
    tipo_rol = SelectField('Rol', coerce=int)
    submit = SubmitField('Registrar')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()], render_kw={"placeholder": "email"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Contraseña"})
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Login')


class RolForm(FlaskForm):
    name = StringField('Nombre del rol', validators=[DataRequired(), Length(max=30)])
    descripcion = StringField('Descripción del rol', validators=[Length(max=100)])
    submit = SubmitField('Registrar')
