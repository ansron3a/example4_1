import json

from flask import Flask, request, url_for, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def start():
    return render_template('index.html', css_path=url_for('static', filename='css/index_style.css'))

# Вывод всех сотрудников
@app.route('/employees')
def employees():
    with open(url_for('static', filename='data/organization.json')[1:], 'rt', encoding='utf-8') as f:
        org_list = json.loads(f.read())
    return render_template('employees.html', org=org_list, css_path=url_for('static', filename='css/emp_style.css'))

# Вывод сотрудника по id
@app.route('/employee/<int:id>')
def employee(id=None):
    with open(url_for('static', filename='data/organization.json')[1:], 'rt', encoding='utf-8') as f:
        org_list = json.loads(f.read())
    return render_template('employee.html', org=org_list,
                           css_path=url_for('static', filename='css/emp_style.css'), id=id)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')