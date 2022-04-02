from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

class Member(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    pwd = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)

class Hospital(db.Model):
    num = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(40), nullable=False)
    tel = db.Column(db.String(20), nullable=False)
    latitude = db.Column(db.Numeric)
    longitude = db.Column(db.Numeric)

class HospService:
    def addHosp(self, h:Hospital):
        db.session.add(h)
        db.session.commit()

    def getAll(self):
        return Hospital.query.order_by(Hospital.num.asc())

class MemService:
    def join(self, m:Member):#회원가입
        db.session.add(m)   #insert구문실행
        db.session.commit() # 쓰기 작업 커밋

    def login(self, id:str, pwd:str):#로그인
        mem = Member.query.get(id) # primary key 기준으로 select
        if mem is not None:
            if pwd == mem.pwd:
                session['login_id']=id
                session['flag']=True
                return True

        return False

    def myInfo(self):#로그인 한 id로 검색한 객체 반환
        id = session['login_id']
        return Member.query.get(id)

    def editMyInfo(self, pwd:str): #새 pwd받아서 현재 로그인 중인 id 검색하여 수정
        mem = self.myInfo()
        mem.pwd = pwd   # 수정할 객체의 멤버변수를 수정하면 테이블 컬럼값도 수정됨
        db.session.commit() ## 쓰기 완료

    def logout(self):#session에서 id 삭제 및 flag =False로 변환
        session.pop('login_id')
        session['flag']=False

    def out(self):#로그인한 id를 db에서 삭제. 로그아웃 처리.
        mem = self.myInfo()
        db.session.delete(mem) # delete문 실행. 파라메터로 삭제할 객체 지정
        db.session.commit()
        self.logout()