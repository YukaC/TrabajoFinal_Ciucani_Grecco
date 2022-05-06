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

@app.route('/')
def hello_world():
    return 'Allá te vamos netflix(?)'

@app.route('/peliculas', methods=['GET'])
def allfilms():
    peliculas = db['peliculas']
    generos = db['generos']
    directores = db['directores']
    respuesta = []
    for pelicula in peliculas:
        for genero in generos:
            if (pelicula['genero'] == genero['id']):
                pelicula['genero'] = genero['nombre']
            if (pelicula['genero2'] == genero['id']):
                pelicula['genero2'] = genero['nombre']
        for director in directores:
            if (pelicula['director'] == director['id']):
                pelicula['director'] = director['nombre']
            if (pelicula['director2'] == director['id']):
                pelicula['director2'] = director['nombre']
        respuesta.append(pelicula)
    return jsonify(respuesta)
    # return jsonify(request.args.get('director'))

@app.route('/ultimas-peliculas', methods=['GET'])
def last10():
        peliculas = db['peliculas'][-10:]
        generos = db['generos']
        directores = db['directores']
        respuesta = []
        for pelicula in peliculas:
            for genero in generos:
                if (pelicula['genero'] == genero['id']):
                    pelicula['genero'] = genero['nombre']
                if (pelicula['genero2'] == genero['id']):
                    pelicula['genero2'] = genero['nombre']
            for director in directores:
                if (pelicula['director'] == director['id']):
                    pelicula['director'] = director['nombre']
                if (pelicula['director2'] == director['id']):
                    pelicula['director2'] = director['nombre']
            respuesta.append(pelicula)
        return jsonify(respuesta)

@app.route('/peliculas/<id>', methods=['GET'])
def films_by_id(id):
        id = int(id)
        for pelicula in db['peliculas']:
            if pelicula['id'] == id:
                return jsonify(pelicula)
            

@app.route('/director/<id>', methods=['GET'])
def allfilmsbydirector(id):
    id = int(id)
    peliculas_by_dir = []
    for pelicula in db['peliculas']:
         if (pelicula['director'] == id or pelicula['director2'] == id):
            peliculas_by_dir.append(pelicula)
    return jsonify(peliculas_by_dir)


@app.route("/genero/<id>", methods=['GET'])
def all_films_by_gender(id):
    id = int(id)
    peliculas_by_gen = []
    for pelicula in db['peliculas']:
         if (pelicula['genero'] == id or pelicula['genero2'] == id):
            peliculas_by_gen.append(pelicula)
    return jsonify(peliculas_by_gen)
            
 
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
    return jsonify(db['peliculas'][-3:][random.randint(0,2)])

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
def login_user(): #devolver los datos del usuario
    data_user = request.form
    username = data_user.get('username')
    password = data_user.get('password')
    for user in db['usuarios']:
        if user['nombre'] == username and user['passw'] == password:
            return jsonify("loggedIn"),HTTPStatus.OK
    return ("LoggedOut"),HTTPStatus.UNAUTHORIZED

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
            return jsonify(False), HTTPStatus.CONFLICT
        else :
            pelicula = {
                'id': len(db['peliculas']) + 1,
                'nombre': nombre_pelicula,
                'sinopsis': sinopsis,
                'genero': int(genero),
                'genero2': int(genero2),
                'director': int(director),
                'director2': int(director2),
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
    
    for pelicula in db['peliculas']:
        if pelicula['id'] == int(id):
            pelicula['nombre'] = nombre_pelicula
            pelicula['sinopsis'] = sinopsis
            pelicula['genero'] = genero
            pelicula['genero2'] = genero2
            pelicula['director'] = director
            pelicula['director2'] = director2
            pelicula['duracion'] = duracion
            pelicula['year'] = year
            pelicula['score'] = score
            return jsonify(pelicula), HTTPStatus.OK
    return HTTPStatus.NOT_FOUND
        
@app.route('/eliminar-pelicula/<id>', methods=["DELETE"])
def delete_film(id):
    for pelicula in db['peliculas']:
        if pelicula['id'] == int(id):
            for comentario in db['comentarios']:
                if comentario['pelicula'] == pelicula['id']:
                    return HTTPStatus.CONFLICT
            db['peliculas'].remove(pelicula)
            return jsonify(pelicula), HTTPStatus.OK
    return HTTPStatus.NOT_FOUND
    
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
            db['comentarios'].append(comentario)
            return jsonify(comentario), HTTPStatus.OK
    
@app.route('/buscar', methods=["GET"])
def search():
    respuesta = []
    for pelicula in db['peliculas']:
        if pelicula['nombre'].lower().find(request.args.get('input').lower()) != -1:
            respuesta.append(pelicula)
    return jsonify(respuesta)
      
app.run()