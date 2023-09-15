from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# from app import User


app = Flask(__name__)
# SQLiteデータベースのファイルパス
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# アプリケーションコンテキストを設定
# app.app_context().push()

# データベースモデルを定義


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# 以下のコードは後で追加します


@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # データベースにユーザーを追加
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # ユーザー認証のロジックを追加することができます

        return 'ログイン成功'  # ユーザー認証が成功した場合の処理を追加

    return render_template('login.html')


@app.route('/users', methods=['GET'])
def list_users():
    users = User.query.all()  # ユーザーをデータベースから取得
    return render_template('user_list.html', users=users)


if __name__ == '__main__':
    app.app_context().push()
    db.create_all()  # データベースの初期化
    app.run(debug=True)
