from app import login_manager, db
from . import pedido_bp
from .model import Asociados, Clientes
from .forms import AsociadoForm, ClienteForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from flask import render_template, redirect, url_for, request


@pedido_bp.route('/all-asociado/')
def all_asociado():
    asociados = Asociados.query.all()
    return render_template('asociado_all.html', asociados=asociados)


@pedido_bp.route('/edit-asociado/<int:asoc_id>', methods=['GET', 'POST'])
def edit_asociado(asoc_id):
    form = AsociadoForm()
    asociado = Asociados.query.filter_by(id=asoc_id)
    if form.validate_on_submit():
        asociado.nombre = form.nombre.data
        asociado.telefono = form.telefono.data
        asociado.email = form.email.data
        db.session.commit()
        next_page = request.args.get('next', None)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('pedidos.all_asociado')
        return redirect(next_page)
    return render_template('asociado_edit.html', form=form, obj=asociado)


@pedido_bp.route('/add-asociado/',  methods=['GET', 'POST'])
def add_asociado():
    form = AsociadoForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        telefono = form.telefono.data
        mail = form.email.data
        new_asoc = Asociados(nombre=nombre, telefono=telefono, email=mail)
        db.session.add(new_asoc)
        db.session.commit()
        next_page = request.args.get('next', None)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('pedidos.all_asociado')
        return redirect(next_page)
    return render_template('asociado_add.html', form=form)


@pedido_bp.route('/all-cliente/')
def all_cliente():
    clientes = Clientes.query.all()
    return render_template('cliente_all.html', clientes=clientes)


@pedido_bp.route('/edit-cliente/<int:cli_id>', methods=['GET', 'POST'])
def edit_cliente(cli_id):
    form = ClienteForm()
    cliente = Clientes.query.filter_by(id=cli_id)
    if form.validate_on_submit():
        cliente.nombre = form.nombre.data
        cliente.ruc = form.ruc.data
        cliente.telefono = form.telefono.data
        cliente.email = form.email.data
        db.session.commit()
        next_page = request.args.get('next', None)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('pedidos.all_cliente')
        return redirect(next_page)
    return render_template('cliente_edit.html', form=form, obj=cliente)


@pedido_bp.route('/add-cliente/',  methods=['GET', 'POST'])
def add_cliente():
    form = ClienteForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        ruc = form.ruc.data
        telefono = form.telefono.data
        mail = form.email.data
        direccion = form.direccion.data
        asociado = form.asociado.data
        new_cli = Asociados(nombre=nombre, ruc=ruc, telefono=telefono,
                            email=mail, direccion=direccion, id_asociado=asociado)
        db.session.add(new_cli)
        db.session.commit()
        next_page = request.args.get('next', None)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('pedidos.all_cliente')
        return redirect(next_page)
    return render_template('cliente_add.html', form=form)
