from flask import Blueprint, render_template, request, flash, redirect, url_for
bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@bp.route('/creator', methods=['GET'])
def creator():
    return render_template('creator.html')

@bp.route('/eta', methods=['GET'])
def eta():
    return render_template('eta.html')

@bp.route('/gruppo', methods=['GET'])
def gruppo():
    return render_template('gruppoFamigliare.html')
