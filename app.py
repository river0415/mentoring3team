from flask import Flask, render_template
# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy
from models import db, migrate
import routes.hosp_route as hr
import routes.mem_route as mr

import config

app = Flask(__name__)
app.config.from_object(config)

app.register_blueprint(hr.bp)
app.register_blueprint(mr.bp)


migrate.init_app(app, db)


db.init_app(app)
@app.route('/')
def root():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()#flask 서버 실행