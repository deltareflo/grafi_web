from app import login_manager, db
from . import pedido_bp
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from flask import render_template, redirect, url_for, request

