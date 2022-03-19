from flask import request, render_template, redirect, Blueprint, session
from models import HospService, Hospital

service = HospService()

bp = Blueprint('hospital', __name__, url_prefix='/hosp')

@bp.route('/list')
def list():
    hlist = service.getAll()
    return render_template('hosp/list.html', hlist=hlist)

@bp.route('/add')
def addForm():
    return render_template('hosp/form.html')

@bp.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    address = request.form['address']
    tel = request.form['tel']
    service.addHosp(Hospital(name=name, address=address, tel=tel))
    return redirect('/hosp/list')