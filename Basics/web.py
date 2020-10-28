# from bottle import route, run, template

# @route('/hello/<name>')
# def index(name):
#   return template('<p>Hello {{name}}</p>', name=name)

# run(host='localhost', port=8080)

from bottle import Bottle, run

app = Bottle()

msg = '''
<center><h1>Minha página web</h1></center>
<p>Python tb pode ser usado para fazer um backend maneiro</p>
<center><a href="/curso_python">Clique aqui pra acessar o curso</a></center>
'''

@app.route('/')
def index():
  return msg

@app.route('/curso_python')
def curso():
  return '<center><h1>Benvindo</h1></center>\
          <center><a href="/">Voltar a pagina principal</a></center>'

run(app, host='localhost', port=8080)