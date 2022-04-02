from flask import Flask, render_template
# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy
from models import db, migrate
import routes.hosp_route as hr

import config

# db = SQLAlchemy()
# migrate = Migrate()

app = Flask(__name__) # flask 객체 생성. 웹 서버를 포함한 app

#시크릿 키 생성
app.secret_key = 'asfaf'

app.config.from_object(config)

app.register_blueprint(hr.bp)
app.register_blueprint(mr.bp)

db.init_app(app)
migrate.init_app(app, db)

@app.route('/')
def root():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()#flask 서버 실행