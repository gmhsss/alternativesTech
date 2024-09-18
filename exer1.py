from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return """
    <html>
<head>
<title>Componentes</title>
</head>
<body>
<h1>Pagina Inicial</h1>

<li> Entrar para <a href="/actuators">atuadores </a>!
<li> Entrar para <a href="/sensors">sensores </a>!


</p>
</body>
</html>
"""


@app.route('/sensors')
def sensors():
    return """
    <html>
    <body>
    <h1>Sensores</h1>
    <ul>
    <li>Sensor de Umidade</li>
    <li>Sensor de Temperatura</li>
    <li>Sensor de Luminosidade</li>
    </ul>
    <li> Entrar para <a href="/actuators">atuadores </a>!
    <li> Voltar para <a href="/">pagina inicial </a>!


    </p>
    </body>
    </html>"""

@app.route('/actuators')
def actuators():
    return """
    <html>
<head>
<title>Minha Casa</title>
</head>
<body>
<h1>Atuadores</h1>
<ul>
<li>Servo Motor</li>
<li>Lampada</li>
</ul>
<li> Entrar para <a href="/sensors">sensores </a>!
<li> Voltar para <a href="/">pagina inicial </a>!

</p>
</body>
</html>
"""




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)