from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title="Flask", mensaje="Bienvenido a la biblioteca ICO")

@app.route('/servicios')
def servicios():
    return render_template('servicios.html', title="Servicios", mensaje="Estos son los servicios que ofrecemos, durante el horario disponible de atención al público.")

@app.route('/contacto')
def contacto():
    return render_template('contacto.html', title="Contacto", mensaje="Contáctanos para más información.")

@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html', title="Catálogo", mensaje="Contamos con una amplia selección de libros en diferentes categorías.")

if __name__ == '__main__':
    app.run(debug=True, port=5050)