from flask import render_template, request, Blueprint
from models import MemService, Member

service = MemService()

bp = Blueprint('member', __name__, url_prefix='/member') #라우트 등록 객체

@bp.route('/login', methods=['GET'])  # /login이고 get방식 요청 오면 처리
def loginForm():
    return render_template('member/loginForm.html')

@bp.route('/login', methods=['POST']) # /login이고 post방식 요청 오면 처리
def login():
    id = request.form['id'] # 요청 파라메터 이름이 'id'인 값 읽기
    pwd = request.form['pwd'] # 요청 파라메터 이름이 'pwd'인 값 읽기
    flag = service.login(id, pwd)
    return render_template('index.html')

@bp.route('/join')
def joinForm():
    return render_template('member/joinForm.html')

@bp.route('/join', methods=['POST'])
def join():
    id = request.form['id']
    pwd = request.form['id']
    name = request.form['name']
    email = request.form['email']
    service.join(Member(id=id, pwd=pwd, name=name, email=email))
    return render_template('member/loginForm.html')

@bp.route('/myinfo')
def myinfo():
    m = service.myInfo()
    return render_template('member/detail.html', m=m)

@bp.route('/out')
def out():
    service.out()
    return render_template('index.html')

@bp.route('/edit', methods=['POST'])
def edit():
    pwd = request.form['pwd']
    service.editMyInfo(pwd)
    return render_template('index.html')