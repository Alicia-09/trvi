from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    mensaje = "<h1> ¡Bienvenido a la calculadora de Flask!</h1>"
    
    mensaje += "<h2> Para poder usarla tendras que hacer</h2>"
    mensaje += "<ol>"
    mensaje += "<li><h2>Sumar http://127.0.0.1:5000//sumar/10/20</h2></li>"
    mensaje += "<li><h2>Restar http://127.0.0.1:5000/restar/10/20</h2></li>"
    mensaje += "<li><h2>Multiplicar http://127.0.0.1:5000/multiplicar/10/20</h2></li>"
    mensaje += "<li><h2>Dividir http://127.0.0.1:5000/dividir/10/20</h2></li>"
    mensaje += "<li><h2>Maximo http://127.0.0.1:5000/maximo/10/20</h2></li>"
    mensaje += "<li><h2>Minimo http://127.0.0.1:5000/minimo/10/20</h2></li>"
    mensaje += "</ol>"
    return mensaje

@app.route("/sumar/<v1>/<v2>")
def sumar1(v1,v2):
    s=str(float(v1)+ float (v2))
    mensaje= f"<h1>La suma de {v1} + {v2} es {s}</h1>"
    return mensaje

@app.route("/restar/<v1>/<v2>")
def restar1(v1,v2):
    r=str(float(v1) - float (v2))
    mensaje= f"<h1>La resta de {v1} - {v2} es {r}</h1>"
    return mensaje

@app.route("/multiplicar/<v1>/<v2>")
def multiplicar1(v1,v2):
    m=str(float(v1) *  float (v2))
    mensaje= f"<h1>La multiplicacion de {v1} * {v2} es {m}</h1>"
    return mensaje

@app.route("/dividir/<v1>/<v2>")
def dividir1(v1,v2):
    d=str(float(v1) / float (v2))
    mensaje= f"<h1>La division de {v1} / {v2} es {d}</h1>"
    return mensaje

@app.route("/maximo/<v1>/<v2>")
def maximo1(v1,v2):
    n1 = float(v1)
    n2 = float(v2)
    if n1 > n2:
        mayor = n1
    else:
        mayor = n2
    mensaje= f"<h1>El maximo entre {n1} y  {n2} es {mayor}</h1>"
    return mensaje

@app.route("/minimo/<v1>/<v2>")
def minimo1(v1,v2):
    n1 = float(v1)
    n2 = float(v2)
    if n1 < n2:
        menor = n1
    else:
        menor = n2
    mensaje= f"<h1>El minimo entre {n1} y  {n2} es {menor}</h1>"
    return mensaje

if __name__ == "__main__":
    app.run(debug=True)