from models import *


class Asociados(db.Model, TimestampMixin):
    __table_name__= 'grafi_asociados'
    id = db.Column(Integer, primary_key=True)
    nombre = db.Column(String(length=40), nullable=False, unique=True)
    telefono = db.Column(Integer)
    email = db.Column(String(length=150))
    contacto = db.relationship('Clientes', backref='clientes_user', lazy=True)

    def __repr__(self):
        return f'<Asociado {self.nombre}>'


class Clientes(db.Model, TimestampMixin):
    __table_name__ = 'grafi_clientes'
    id = db.Column(Integer, primary_key=True)
    nombre = db.Column(String(length=40), nullable=False)
    ruc = db.Column(String(length=12), nullable=False, unique=True)
    telefono = db.Column(Integer)
    email = db.Column(String(length=150))
    direccion = db.Column(String(length=150))
    # ForeignKey
    id_asociado = db.Column(Integer, ForeignKey('grafi_asociados.id'))

    def __repr__(self):
        return f'<Cliente {self.nombre}>'


class TipoPapeles(db.Model, TimestampMixin):
    __table_name__ = 'tipo_papeles'
    id = db.Column(Integer, primary_key=True)
    nombre = db.Column(String(length=40), nullable=False, unique=True)
    descripcion = db.Column(String(length=150), nullable=False)

    def __repr__(self):
        return f'<Tipo papel {self.nombre}>'


class Proveedor(db.Model, TimestampMixin):
    __table_name__ = 'proveedor'
    id = db.Column(Integer, primary_key=True)
    nombre = db.Column(String(length=40), nullable=False, unique=True)
    telefono = db.Column(Integer)
    email = db.Column(String(length=150))

    def __repr__(self):
        return f'<Proveedor {self.nombre}>'


class Papeles(db.Model, TimestampMixin):
    __table_name__ = 'papeles'
    id = db.Column(Integer, primary_key=True)
    nombre = db.Column(String(length=40), nullable=False, unique=True)
    descripcion = db.Column(String(length=150), nullable=False)
    ancho = db.Column(Integer, nullable=False)
    largo = db.Column(Integer, nullable=False)
    gramaje = db.Column(Integer, nullable=False)
    precio = db.Column(Integer)
    # ForeignKey
    id_tipo = db.Column(Integer, ForeignKey('tipo_papeles.id'))
    tipo_papel = db.relationship('TipoPapeles', backref='papeles', lazy=True)
    id_proveedor = db.Column(Integer, ForeignKey('proveedor.id'))
    proveedor = db.relationship('Proveedor', backref='proveedor_user', lazy=True)
    producto = db.relationship('Productos', backref='papeles', lazy=True)

    def __repr__(self):
        return f'<Papeles {self.nombre}>'


class Productos(db.Model, TimestampMixin):
    __table_name__ = 'productos'
    id = db.Column(Integer, primary_key=True)
    nombre = db.Column(String(length=40), nullable=False, unique=True)
    descripcion = db.Column(String(length=150), nullable=False)
    ancho = db.Column(Integer, nullable=False)
    largo = db.Column(Integer, nullable=False)
    precio = db.Column(Integer, nullable=False)
    # ForeignKey
    id_papeles = db.Column(Integer, ForeignKey('papeles.id'))

    def __repr__(self):
        return f'<Producto {self.nombre}>'


class PresupuestoHead(db.Model, TimestampMixin):
    __table_name__ = 'presupuesto_cabecera'
    id = db.Column(Integer, primary_key=True)
    # ForeignKey
    id_cliente = db.Column(Integer, ForeignKey('grafi_clientes.id'))
    presupuesto_det = db.relationship('PresupuestoDet', backref='presu_cabecera', lazy=True)

    def __repr__(self):
        return f'<Presupuesto {self.nombre}>'


class PresupuestoDet(db.Model, TimestampMixin):
    __table_name__ = 'presupuesto_det'
    id = db.Column(Integer, primary_key=True)
    cantidad = db.Column(Integer, nullable=False)
    precio = db.Column(Integer, nullable=False)
    # Foreign Key
    id_producto = db.Column(Integer, ForeignKey('productos.id'))
    id_presu_head= db.Column(Integer, ForeignKey('presupuesto_cabecera.id'))

