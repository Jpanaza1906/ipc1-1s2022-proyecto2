from flask import Blueprint, jsonify, request
from db.database import lbDatabase
from prestamista.models.prestamista_model import Prestamista

prestamista = Blueprint('prestamista', __name__, url_prefix='/person')

@prestamista.route('', methods = ['POST'])
def crear():
    body = request.get_json()
    try:
        if("cui" in body and "last_name" in body and "first_name" in  body):
            if(body["cui"] != "" and body["last_name"] != "" and body["first_name"] != ""):
                prestamista = Prestamista(body["cui"], body["last_name"],body["first_name"],False)
                if(lbDatabase.agregarPrestamista(prestamista)):
                    return{'msg': "Prestamista creado existosamente"}, 200
                else:
                    return{'msg': 'El CUI ya se encuentra registrado.'}, 404
            else:
                return{'msg': 'Los campos deben tener contenido.'}, 404
        else:
            return{'msg': 'Asegurese de introducir correctamente TODOS los campos'},404
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500
    
@prestamista.route('/<cui>', methods = ['GET'])
def ver(cui):
    try:
        if(cui != None):
            historialp = lbDatabase.consultarPrestamos(cui)
            return jsonify(historialp), 200
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500