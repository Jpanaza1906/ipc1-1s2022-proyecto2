from flask import Blueprint, jsonify, request
from db.database import lbDatabase
from prestamo.models.prestamo_model import Prestamo

prestamo = Blueprint('prestamo', __name__, url_prefix='/borrow')

@prestamo.route('', methods = ['POST'])
def prestar():
    body = request.get_json()
    try:
        if("cui" in body and "isbn" in body):
            if(body["cui"] != "" and body["isbn"] != None):
                prestamo = Prestamo(body["cui"], body["isbn"])
                lprestado = lbDatabase.prestarLibro(prestamo)
                if(lprestado == "i"):
                    return {'msg': 'El CUI no fue encontrado en los registros.'}, 404                    
                elif(lprestado == "e"):
                    return {'msg': 'El ISBN no fue encontrado en los registros'}, 404
                elif(lprestado == None):
                    return {'msg': 'El prestamista no puede prestar libros hasta que devuelva el pendiente'}, 404
                else:
                    return jsonify(lprestado), 200                
            else:
                return{'msg': 'Los campos deben tener contenido.'}, 404                
        else:
            return{'msg': 'Asegurese de introducir correctamente TODOS los campos'},404                   
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500

@prestamo.route('/borrow/<uuid>', methods = ['PATCH'])
def devolver():
    return