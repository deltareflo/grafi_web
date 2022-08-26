from flask import Blueprint

pedido_bp = Blueprint('pedido', __name__, template_folder="templates")

from . import pedidos