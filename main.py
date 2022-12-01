import json

from flask import Flask, request, url_for, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def start():
    return render_template('index.html', css_path=url_for('static', filename='css/index_style.css'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')