from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    rotas = {'Quarto': '/Quarto', 'Banheiro': '/Banheiro'}
    return render_template("index.html", rotas=rotas)


@app.route('/Quarto')
def quarto():
     devices = ['Luminosidade', 'Interruptores']
     return render_template("quarto.html", devices=devices)

@app.route('/Banheiro')
def banheiro():
    devices = ['Umidade', 'Lampadas']
    return render_template("banheiro.html", devices=devices)






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)