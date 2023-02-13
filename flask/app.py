# Importamos la libreria Flask para crear la API
from flask import Flask, jsonify, request
# Importamos la libreria HTTPStatus para poder usar los codigos de estado
from http import HTTPStatus
# Importar la libreria CORS para que se pueda hacer peticiones desde cualquier origen
from flask_cors import CORS

import json

app = Flask(__name__)
CORS(app)

with open('db.json', encoding='utf-8') as json_file:
    db = json.load(json_file)
logged_In = False
parsed_films = db['peliculas'].copy()

@app.route('/')
def hello_world():
    return 'Allá te vamos netflix(?)'

@app.route('/peliculas', methods=['GET'])
def allfilms():
    if logged_In == True:
        peliculas = db['peliculas']
    else:
        peliculas = db['peliculas'][-10:]
    generos = db['generos']
    directores = db['directores']
    respuesta = []
    for pelicula in peliculas:
        parsed_film = pelicula.copy()
        for genero in generos:
            if (pelicula['genero'] == genero['id']):
                parsed_film['genero'] = genero['nombre']
            if (pelicula['genero2'] == genero['id']):
                parsed_film['genero2'] = genero['nombre']
        for director in directores:
            if (pelicula['director'] == director['id']):
                parsed_film['director'] = director['nombre']
            if (pelicula['director2'] == director['id']):
                parsed_film['director2'] = director['nombre']
        respuesta.append(parsed_film)
    return jsonify(respuesta)

@app.route('/peliculas/<id>', methods=['GET'])
def films_by_id(id):
        id = int(id)
        generos = db['generos']
        directores = db['directores']
        for pelicula in db['peliculas']:
            if pelicula['id'] == id:
                parsed_film = pelicula.copy()
                for genero in generos:
                    if (pelicula['genero'] == genero['id']):
                        parsed_film['genero'] = genero['nombre']
                    if (pelicula['genero2'] == genero['id']):
                        parsed_film['genero2'] = genero['nombre']
                for director in directores:
                    if (pelicula['director'] == director['id']):
                        parsed_film['director'] = director['nombre']
                    if (pelicula['director2'] == director['id']):
                        parsed_film['director2'] = director['nombre']
                return jsonify(parsed_film)                  
 
@app.route('/imagen', methods=['GET'])
def allfilmswithimage():
    filmswimg=[]
    for pelicula in db['peliculas']:
        try :
            f=open("./static/" + str( pelicula['id'])+'.jpg')
            filmswimg.append(pelicula)
            f.close()
        except FileNotFoundError:
            continue
            
    return jsonify(filmswimg)
    
@app.route("/directores", methods=['GET'])
def alldirectors():
    return jsonify(db['directores'])
    
@app.route("/generos", methods=['GET'])
def allgenders():
    return jsonify(db['generos'])

@app.route('/random', methods=['GET'])
def random_last_3():
    import random
    generos = db['generos']
    directores = db['directores']
    respuesta = []
    peliculas = db['peliculas']
    for pelicula in peliculas:
        parsed_film = pelicula.copy()
        for genero in generos:
            if (pelicula['genero'] == genero['id']):
                parsed_film['genero'] = genero['nombre']
            if (pelicula['genero2'] == genero['id']):
                parsed_film['genero2'] = genero['nombre']
        for director in directores:
            if (pelicula['director'] == director['id']):
                parsed_film['director'] = director['nombre']
            if (pelicula['director2'] == director['id']):
                parsed_film['director2'] = director['nombre']
        respuesta.append(parsed_film)
    return jsonify(respuesta[-3:][random.randint(0,2)])

@app.route('/peliculas/<id>/comentarios', methods=['GET'])
def comments_by_films(id):
    id = int(id)
    comentarios = db['comentarios']
    respuesta = []
    for comentario in comentarios:
            if (comentario['pelicula'] == id):              
                respuesta.append(comentario)
    return jsonify(respuesta)

@app.route('/login-user', methods=["POST"])
def login_user():
    global logged_In
    data_user = request.form
    username = data_user.get('username')
    password = data_user.get('password')
    for user in db['usuarios']:
        if user['nombre'] == username and user['passw'] == password:
            logged_In = True
            return jsonify("loggedIn"),HTTPStatus.OK
    logged_In = False
    return ("LoggedOut"),HTTPStatus.UNAUTHORIZED

@app.route('/logout-user', methods=["POST"])
def logout_user():
    global logged_In
    logged_In = False
    return jsonify("loggedOut"),HTTPStatus.OK

@app.route('/subir-pelicula', methods=["POST"])
def add_film():
    data_user = request.form
    
    nombre_pelicula = data_user.get('nombre_pelicula')
    sinopsis = data_user.get('sinopsis')
    genero = data_user.get('genero')
    genero2 = data_user.get('genero2')
    director = data_user.get('director')
    director2 = data_user.get('director2')
    duracion = data_user.get('duracion')
    year = data_user.get('year')
    score = data_user.get('score')
    
    for film in db['peliculas']:
        if film['nombre'] == nombre_pelicula:
            return jsonify("Ese nombre ya existe"), HTTPStatus.CONFLICT
        else :
            pelicula = {
                'id': len(db['peliculas']) + 1,
                'nombre': nombre_pelicula,
                'sinopsis': sinopsis,
                'genero': int (genero),
                'genero2': int (genero2),
                'director': int (director),
                'director2': int (director2) if director2 else None,
                'duracion': duracion,
                'year': year,
                'score': score,
                'img': 'img_default.jpg',
            }
            db['peliculas'].append(pelicula)
            return jsonify(db['peliculas']), HTTPStatus.OK
        
@app.route('/editar-pelicula/<id>', methods=["POST"])
def edit_film(id):
    data = request.form
    nombre_pelicula = data.get('nombre_pelicula')
    sinopsis = data.get('sinopsis')
    genero = data.get('genero')
    genero2 = data.get('genero2')
    director = data.get('director')
    director2 = data.get('director2')
    duracion = data.get('duracion')
    year = data.get('year')
    score = data.get('score')
    
    if logged_In==True:
        for pelicula in db['peliculas']:
            if pelicula['id'] == int(id):
                pelicula['nombre'] = nombre_pelicula
                pelicula['sinopsis'] = sinopsis
                pelicula['genero'] = int (genero)
                pelicula['genero2'] = int (genero2)
                pelicula['director'] = int (director)
                pelicula['director2'] = int (director2) if director2 else None
                pelicula['duracion'] = duracion
                pelicula['year'] = year
                pelicula['score'] = score
                return jsonify(pelicula), HTTPStatus.OK
        return jsonify("Esa pelicula no existe"),HTTPStatus.NOT_FOUND
    return jsonify("Debes estar logueado para editar una pelicula"),HTTPStatus.UNAUTHORIZED

@app.route('/mostrar-pelicula/<id>', methods=['GET'])
def edit_film_show(id):
    for pelicula in db['peliculas']:
        if pelicula['id'] == int(id):
            return jsonify(pelicula), HTTPStatus.OK
    return jsonify("La pelicula no existe"),HTTPStatus.NOT_FOUND
        
@app.route('/eliminar-pelicula/<id>', methods=["DELETE"])
def delete_film(id):
    for pelicula in db['peliculas']:
        if pelicula['id'] == int(id):
            for comentario in db['comentarios']:
                if comentario['pelicula'] == pelicula['id']:
                    return HTTPStatus.CONFLICT
            if logged_In == True:
                db['peliculas'].remove(pelicula)
                return jsonify(pelicula), HTTPStatus.OK
            else:
                return jsonify("Error, no puedes eliminar una pelicula si no estás logueado"),HTTPStatus.UNAUTHORIZED
    return jsonify("Error al eliminar, pelicula no encontrada"),HTTPStatus.NOT_FOUND
    
@app.route('/subir-comentario', methods=["POST"])
def add_comment():
    data_user = request.form
    film_id = data_user.get('film_id')
    comentario = data_user.get('comment')
    usuario = data_user.get('username')
    fecha = data_user.get('comment_date')
    for pelicula in db['peliculas']:
        if pelicula['id'] == int(film_id):
            comentario = {
                'id': len(db['comentarios']) + 1,
                'pelicula': int(film_id),
                'texto': comentario,
                'usuario': usuario,
                'hora': fecha,
            }
            if logged_In==True:
                db['comentarios'].append(comentario)
                return jsonify(comentario), HTTPStatus.OK
            else:
                return jsonify("Debes estár logueado para comentar"),HTTPStatus.UNAUTHORIZED
    
@app.route('/buscar', methods=["GET"])
def search():
    respuesta = []
    data = db['peliculas'] if logged_In == True else db['peliculas'][-10:]
    for pelicula in data:
        if pelicula['nombre'].lower().find(request.args.get('input').lower()) != -1:
            respuesta.append(pelicula)
    return jsonify(respuesta), HTTPStatus.OK

@app.route('/filtrar', methods=['GET'])
def filter():
    generos = db['generos']
    directores = db['directores']
    respuesta = []
    genero = request.args.get('genero')
    director = request.args.get('director')
    data = db['peliculas'] if logged_In == True else db['peliculas'][-10:]
        
    for pelicula in data:
        parsed_film = pelicula.copy()
        if int(genero) == 0 and int(director) != 0 and (parsed_film['director'] == int(director) or parsed_film['director2'] == int(director)):
            respuesta.append(parsed_film)
        elif int(director) == 0 and int(genero) != 0 and (parsed_film['genero'] == int(genero) or parsed_film['genero2'] == int(genero)):
            respuesta.append(parsed_film)
        elif int(genero) != 0 and int(director) != 0 and ((parsed_film['director'] == int(director) or parsed_film['director2'] == int(director)) and (parsed_film['genero'] == int(genero) or parsed_film['genero2'] == int(genero))):
            respuesta.append(parsed_film)
        elif int(genero) == 0 and int(director) == 0:
            respuesta.append(parsed_film)
    for x in respuesta:
        for genero in generos:
            if (x['genero'] == genero['id']):
                x['genero'] = genero['nombre']
            if (x['genero2'] == genero['id']):
                x['genero2'] = genero['nombre']
        for director in directores:
            if (x['director'] == director['id']):
                x['director'] = director['nombre']
            if (x['director2'] == director['id']):
                x['director2'] = director['nombre']
    return jsonify(respuesta), HTTPStatus.OK

@app.route('/login-check', methods=['GET'])
def login_check():
    log_check = "0"
    if logged_In == True:
        log_check = "1"
        return log_check
    else:
        log_check = "0"
        return log_check
      
app.run()