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
                prestamo = Prestamo(body["cui"], body["isbn"],False)
                lprestado = lbDatabase.prestarLibro(prestamo)
                if(lprestado == "i"):
                    return {'msg': 'El CUI no fue encontrado en los registros.'}, 404 #not found                   
                elif(lprestado == "e"):
                    return {'msg': 'El ISBN no fue encontrado en los registros'}, 404 #not found
                elif(lprestado == "o"):
                    return {'msg': 'El Libro no tiene copias disponibles suficientes'}, 401 #Unauthorized
                elif(lprestado == None):
                    return {'msg': 'El prestamista no puede prestar libros hasta que devuelva el pendiente'}, 401 #Unauthorized
                else:
                    return jsonify(lprestado), 201 #created              
            else:
                return{'msg': 'Los campos deben tener contenido.'}, 400 #bad request
        else:
            return{'msg': 'Asegurese de introducir correctamente TODOS los campos'},400 #bad request                 
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500 #internal server error

@prestamo.route('/<uuid>', methods = ['PATCH'])
def devolver(uuid):
    if uuid !=  None:
        res = lbDatabase.devolverLibro(uuid)
        if(res == True):
            return{'msg': "Se devolvió el libro existosamente"}, 200 #ok
        elif(res == 'ya'):
            return{'msg': "El libro ya se ha devuelto antes"}, 202 #accepted
        else:
            return{'msg': 'El uuid no coincide con los datos registrados.'}, 404 #notfound
    else:
        return{'msg': 'Asegurese de introducir correctamente TODOS los campos'},400 #bad request