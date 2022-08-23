from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, BooleanField, TextAreaField,\
    DateTimeField, SelectField
from wtforms.validators import DataRequired, Email, Length


class AsociadoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=40)])
    telefono = IntegerField('Telefono', render_kw={"placeholder": "0971553022"})
    email = StringField('Email', validators=[Email()])
    submit = SubmitField('Registrar')


class ClienteForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=40)])
    ruc = StringField('RUC', validators=[DataRequired(), Length(max=12)])
    telefono = IntegerField('Telefono', render_kw={"placeholder": "0971553022"})
    email = StringField('Email', validators=[Email()])
    direccion = StringField('Dirección', validators=[Length(max=150)])
    asociado = SelectField('Asociado', coerce=int)
    submit = SubmitField('Registrar')


class TipoPapelForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=40)])
    descripcion = StringField('Descripción', validators=[DataRequired(), Length(max=150)])
    submit = SubmitField('Registrar')


class ProveedorForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=40)])
    telefono = IntegerField('Telefono', render_kw={"placeholder": "0971553022"})
    email = StringField('Email', validators=[Email()])
    submit = SubmitField('Registrar')


class PapelesForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=40)])
    descripcion = StringField('Descripción', validators=[DataRequired(), Length(max=150)])
    ancho = IntegerField('Ancho', validators=[DataRequired()], render_kw={"placeholder": "81"})
    largo = IntegerField('Largo', validators=[DataRequired()], render_kw={"placeholder": "116"})
    gramaje = IntegerField('Gramaje', validators=[DataRequired()], render_kw={"placeholder": "80"})
    precio = IntegerField('Largo', render_kw={"placeholder": "1512"})
    tipo_papel = SelectField('Tipo papel', coerce=int)
    proveedor = SelectField('Proveedor', coerce=int)
    submit = SubmitField('Registrar')


class ProductoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=40)])
    descripcion = StringField('Descripción', validators=[DataRequired(), Length(max=150)])
    ancho = IntegerField('Ancho', validators=[DataRequired()], render_kw={"placeholder": "81"})
    largo = IntegerField('Largo', validators=[DataRequired()], render_kw={"placeholder": "116"})
    precio = IntegerField('Largo', render_kw={"placeholder": "1512"})
    papel = SelectField('Papel', coerce=int)
    submit = SubmitField('Registrar')

