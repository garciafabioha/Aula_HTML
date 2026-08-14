from flask import Flask, render_template

# Inicia o flask
app = Flask(__name__)

# Primeira rota usando Flask
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Segunda rota usando Flask
@app.route('/contato', methods=['GET'])
def contato():
    return render_template('contato.html')

# Terceira rota usando Flask
@app.route('/sobre', methods=['GET'])
def sobre():
    return '<h1>Sobre a Empresa </h1>'

# Rodar o projeto
if __name__ == '__main__':
    app.run(debug=True, port=5000)