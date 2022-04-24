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
                    return{'msg': "Prestamista creado existosamente"}, 201 #created
                else:
                    return{'msg': 'El CUI ya se encuentra registrado.'}, 406 #not acceptable
            else:
                return{'msg': 'Los campos deben tener contenido.'}, 400 #bad request
        else:
            return{'msg': 'Asegurese de introducir correctamente TODOS los campos'},400 #bad request
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500 #internal server error
    
@prestamista.route('/<cui>', methods = ['GET'])
def ver(cui):
    try:
        if(cui != None):
            historialp = lbDatabase.consultarPrestamos(cui)
            if(historialp != None):
                return jsonify(historialp), 200 #ok
            else:
                return{'msg': 'No se ha encontrado el CUI en los datos registrados'}, 404 #not found
        else:
            return{'msg': 'Los campos deben tener contenido.'}, 400 #bad request
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500 #internal server error