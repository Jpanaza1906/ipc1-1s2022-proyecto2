from flask import Flask
from flask_cors import CORS
from libro.routes.libro_route import libro
from prestamista.routes.prestamista_route import prestamista
from prestamo.routes.prestamo_route import prestamo
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return{"msg" : "Si trabaja"}

app.register_blueprint(libro)
app.register_blueprint(prestamista)
app.register_blueprint(prestamo)

if __name__ == '__main__':
    app.run(debug=True)