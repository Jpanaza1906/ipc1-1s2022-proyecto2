from crypt import methods
import re
from flask import Blueprint, jsonify, request
from db.database import lbDatabase
from libro.models.libro_model import Libro

libro = Blueprint('libro', __name__, url_prefix="/book")

#------------------------------------------------------------------------

@libro.route('', methods = ['POST'])
def crear():
    body = request.get_json()
    try:
        if("isbn" in body and "autores" in body and "ypubli" in body and "titulo" in body and "edicion" in body and "temas" in body and "descrip" in body and "ncopias" in body and "estanteria" in body and "fila" in body):
            if(body["ncopias"] > 0):
                libro = Libro(body["isbn"],body["autores"],int(body["ypubli"]),body["titulo"],body["edicion"],body["temas"],body["descrip"],int(body["ncopias"]),body["estanteria"],body["fila"])
                if(lbDatabase.agregarLibro(libro)):
                    return{'msg': "Libro '{libro.gettitulo()}' creado existosamente"}, 201
                else:
                    return{'msg': 'Es posible que el ISBN del libro sea incorrecto'}, 404
            else:
                return{'msg': 'Existe un error en el número de copias'}, 404
        else:
            return{'msg': 'Asegurese de introducir correctamente TODOS los campos'},404
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500


    
