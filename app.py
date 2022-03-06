from flask import Flask, render_template

app = Flask(__name__) # flask 객체 생성. 웹 서버를 포함한 app

@app.route('/')
def root():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()#flask 서버 실행