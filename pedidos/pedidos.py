from app import login_manager, db
from . import pedido_bp
from .model import Asociados, Clientes, TipoPapeles, Proveedor, Papeles
from .forms import AsociadoForm, ClienteForm, TipoPapelForm, ProveedorForm, PapelesForm
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
    return render_template('cliente_add.html', form=form, obj=cliente)


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


@pedido_bp.route('/all-tipo-papeles/')
def all_tipo_papeles():
    tipo_papeles = TipoPapeles.query.all()
    return render_template('tipo_papeles_all.html', tipo_papeles=tipo_papeles)


@pedido_bp.route('/edit-tipo-papeles/<int:tp_id>', methods=['GET', 'POST'])
def edit_tipo_papeles(tp_id):
    form = TipoPapelForm()
    tipo_papel = TipoPapeles.query.filter_by(id=tp_id)
    if form.validate_on_submit():
        tipo_papel.nombre = form.nombre.data
        tipo_papel.descripcion = form.descripcion.data
        db.session.commit()
        next_page = request.args.get('next', None)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('pedidos.all_tipo_papeles')
        return redirect(next_page)
    return render_template('tipo_papeles_add.html', form=form, obj=tipo_papel)


@pedido_bp.route('/add-tipo-papeles/',  methods=['GET', 'POST'])
def add_tipo_papeles():
    form = TipoPapelForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        descripcion = form.descripcion.data
        new_tp = TipoPapeles(nombre=nombre, descripcion=descripcion)
        db.session.add(new_tp)
        db.session.commit()
        next_page = request.args.get('next', None)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('pedidos.all_tipo_papeles')
        return redirect(next_page)
    return render_template('tipo_papeles_add.html', form=form)


@pedido_bp.route('/all-proveedores/')
def all_proveedores():
    proveedores = Proveedor.query.all()
    return render_template('proveedores_all.html', proveedores=proveedores)


@pedido_bp.route('/edit-proveedor/<int:prov_id>', methods=['GET', 'POST'])
def edit_proveedor(prov_id):
    form = ProveedorForm()
    proveedor = Proveedor.query.filter_by(id=prov_id)
    if form.validate_on_submit():
        proveedor.nombre = form.nombre.data
        proveedor.telefono = form.telefono.data
        proveedor.email = form.email.data
        db.session.commit()
        next_page = request.args.get('next', None)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('pedidos.all_proveedores')
        return redirect(next_page)
    return render_template('proveedores_add.html', form=form, obj=proveedor)


@pedido_bp.route('/add-proveedor/',  methods=['GET', 'POST'])
def add_proveedor():
    form = ProveedorForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        telefono = form.telefono.data
        email = form.email.data
        new_prov = Proveedor(nombre=nombre, telefono=telefono, email=email)
        db.session.add(new_prov)
        db.session.commit()
        next_page = request.args.get('next', None)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('pedidos.all_proveedores')
        return redirect(next_page)
    return render_template('proveedores_add.html', form=form)


@pedido_bp.route('/all-papeles/')
def all_papeles():
    papeles = Papeles.query.all()
    return render_template('papeles_all.html', papeles=papeles)


@pedido_bp.route('/edit-papel/<int:papel_id>', methods=['GET', 'POST'])
def edit_papel(papel_id):
    form = PapelesForm()
    papel = Papeles.query.filter_by(id=papel_id)
    if form.validate_on_submit():
        papel.nombre = form.nombre.data
        papel.descripcion = form.descripcion.data
        papel.ancho = form.ancho.data
        papel.largo = form.largo.data
        papel.gramaje = form.gramaje.data
        papel.precio = form.precio.data
        papel.id_proveedor = form.proveedor.data
        papel.id_tipo = form.tipo_papel.data
        db.session.commit()
        next_page = request.args.get('next', None)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('pedidos.all_papeles')
        return redirect(next_page)
    return render_template('papeles_add.html', form=form, obj=papel)


@pedido_bp.route('/add-papel/',  methods=['GET', 'POST'])
def add_papel():
    form = PapelesForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        descripcion = form.descripcion.data
        ancho = form.ancho.data
        largo = form.largo.data
        gramaje = form.gramaje.data
        precio = form.precio.data
        proveedor = form.proveedor.data
        tip_papel = form.tipo_papel.data
        new_papel = Papeles(nombre=nombre, descripcion=descripcion, ancho=ancho,
                             largo=largo, gramaje=gramaje, precio=precio,
                             id_proveedor=proveedor, id_tipo=tip_papel)
        db.session.add(new_papel)
        db.session.commit()
        next_page = request.args.get('next', None)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('pedidos.all_papeles')
        return redirect(next_page)
    return render_template('papeles_add.html', form=form)


@pedido_bp.route('/presupuesto/',  methods=['GET', 'POST'])
def presupuesto():
    clientes = Clientes.query.filter_by(status=1)
    if request.method == 'POST':

        presupuesto_head = Papeles.query.all()

    return render_template('presupuesto.html', clientes=clientes)

