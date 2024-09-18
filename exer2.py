from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return """
    <html>
<head>
<title>Minha Casa</title>
</head>
<body>
<h1>Comodos</h1>
<li>  Entrar em <a href="/Quarto"> Quarto </a>!
<li>  Entrar em <a href="/Banheiro"> Banheiro </a>!

</p>
</body>
</html>
"""


@app.route('/Quarto')
def quarto():
     return """
    <html>
<head>
<title>Minha Casa</title>
</head>
<body>
<ul>
<li>Sensor de Luminosidade</li>
<li>Interruptor</li>
</ul>
<li> Voltar para <a href="/"> Comodos </a>!

</p>
</body>
</html>
"""

@app.route('/Banheiro')
def banheiro():
    return """
    <html>
<head>
<title>Minha Casa</title>
</head>
<body>
<h1>Banheiro</h1>
<ul>
<li>Sensor de Umidade</li>
<li>Lampada Inteligente</li>
</ul>
<li> Voltar para <a href="/"> Comodos </a>!

</p>
</body>
</html>
"""





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)