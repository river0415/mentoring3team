from flask import render_template, request, Blueprint, session

bp = Blueprint('member', __name__, url_prefix='/mem')


@bp.route('/login', methods=['GET'])
def login():
    return render_template('member/index2.html')
