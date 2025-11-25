from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods =['POST', 'GET'])
def index():
    if request.method == 'POST':
        nome = request.form['name']
        email = request.form['email']
        mensagem = request.form['message']
        return f'NOME: {nome} | EMAIL: {email} | mensagem: {mensagem}'



    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug = True)