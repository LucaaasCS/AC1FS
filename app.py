import os
from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/")
def main():
    return render_template('lucas.html')


@app.route('/gravar', methods=['POST', 'GET'])
def gravar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    endereco = request.form['endereco']

    if nome and cpf and endereco:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            'insert into lucas (user_name, user_username, user_password) VALUES (%s, %s, %s)', (nome, cpf, endereco))
        conn.commit()
    return render_template('lucas.html')


@app.route('/listar', methods=['POST', 'GET'])
def listar():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(
        'select user_name, user_username, user_password from lucas')
    data = fetchall()
    conn.commit()
    return render_template('lista.html', datas=data)


if __name__ == "__main__":
    app.run(debug=True)


print ("EH U LUCKAOS VIDA")