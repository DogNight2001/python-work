
from bottle import route, run, template

@route('/<name>/<work>')
def index(name,work):
    return template('<b>{{name}}is a very big {{work}}</b>!', name=name,work=work)

run(host='localhost', port=8080)