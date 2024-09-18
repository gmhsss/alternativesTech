from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/Quarto')
def quarto():
     return render_template("quarto.html")

@app.route('/Banheiro')
def banheiro():
    return render_template("banheiro.html")





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)