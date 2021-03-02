from flask import (
    Flask, render_template, request, url_for, redirect
    )
from get_data import get_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    heading = ['年月', '参加回数', '平均', '最高', '最低']
    user = request.form['User']
    url = "https://atcoder.jp/users/" + user + "/history/json"
    data_list = get_data(url)
    return render_template('index.html', heading=heading, data_list=data_list)

if __name__ == "__main__":
    app.run()