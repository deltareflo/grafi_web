from app import login_manager, db
from . import auth_bp
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from flask import render_template, redirect, url_for, request
from .model import Usuarios, Roles
from .forms import LoginForm, SignupForm, RolForm


@auth_bp.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('public.inicio'))


@auth_bp.route('/login/', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('public.inicio'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuarios.get_by_email(form.email.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('public.inicio')
            return redirect(next_page)
    return render_template('auth/sign-in.html', form=form)


@auth_bp.route('/signup/',  methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated and not current_user.is_admin:
        return redirect(url_for('public.inicio'))
    form = SignupForm()
    error = None
    roles = [(b.id, b.nombre) for b in Roles.query.filter_by(status=1)]
    form.tipo_rol.choices = roles
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        telef= form.telefono.data
        password = form.password.data
        rol = form.tipo_rol.data
        # Comprobamos que no hay ya un usuario con ese email
        user = Usuarios.get_by_email(email)
        if user is not None:
            error = f'El email {email} ya está siendo utilizado por otro usuario'
        else:
            # Creamos el usuario y lo guardamos
            user = Usuarios(nombre=name, email=email, telefono=telef, id_rol=rol)
            user.set_password(password)
            user.save()
            # Dejamos al usuario logueado
            login_user(user, remember=True)
            next_page = request.args.get('next', None)
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('public.inicio')
            return redirect(next_page)
    return render_template('auth/sign-up.html', form=form, error=error)


@auth_bp.route('/all-rol')
@login_required
def all_rol():
    roles = Roles.query.all()
    return render_template('auth/roles_all.html', roles=roles)


@auth_bp.route('/rol-add/', methods=["GET", "POST"])
def add_rol():
    form = RolForm()
    if form.validate_on_submit():
        nombre = form.name.data
        descripcion = form.descripcion.data
        new_rol = Roles(nombre=nombre, descripcion=descripcion)
        db.session.add(new_rol)
        db.session.commit()
        next_page = request.args.get('next', None)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('auth.all_rol')
        return redirect(next_page)
    return render_template('auth/roles_add.html', form=form)


@auth_bp.route('/rol-edit/<int:rol_id>', methods=["GET", "POST"])
@login_required
def edit_rol(rol_id):
    form = RolForm()
    rol = Roles.query.filter_by(id=rol_id).first()
    if form.validate_on_submit():
        rol.nombre = form.name.data
        rol.descripcion = form.descripcion.data
        db.session.commit()
        next_page = request.args.get('next', None)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('auth.all_rol')
        return redirect(next_page)
    return render_template('auth/roles_add.html', form=form, rol=rol)


@auth_bp.route('/del-rol/<int:rol_id>', methods=["GET", "POST"])
@login_required
def del_rol(rol_id):
    rol = Roles.query.filter_by(id=rol_id).first()
    if request.method == 'POST':
        rol.status = int(request.form['estado'])
        db.session.commit()
        return redirect(url_for('auth.all_rol'))
    return render_template('auth/roles_del.html', rol=rol, ref=request.referrer)
