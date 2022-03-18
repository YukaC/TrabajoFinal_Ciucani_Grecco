# Importamos la libreria Flask para crear la API
from flask import Flask, jsonify, request
# Importamos la libreria HTTPStatus para poder usar los codigos de estado
from http import HTTPStatus
# Importar la libreria CORS para que se pueda hacer peticiones desde cualquier origen
from flask_cors import CORS

import json

app = Flask(__name__)
CORS(app)

with open('db.json') as json_file:
    db = json.load(json_file)


@app.route('/')
def hello_world():
    return 'Allá te vamos netflix(?)'


@app.route('/peliculas', methods=['GET'])
def all_films():
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


@app.route('/ultimas-peliculas', methods=['GET'])
def last_10():
    return jsonify(db['peliculas'][-10:])


@app.route('/peliculas/<id>', methods=['GET'])
def films_by_id(id):
        id = int(id)
        for pelicula in db['peliculas']:
            if pelicula['id'] == id:
                return jsonify(pelicula)
            

@app.route("/director/<id>", methods=['GET'])
def all_films_by_director(id):
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

@app.route('/ult3', methods=['GET'])
def ult_3():
    return jsonify(db['peliculas'][-3:])

@app.route('/random', methods=['GET'])
def random_last_3():
    import random
    return jsonify(db['peliculas'][-3:][random.randint(0,2)])
    
app.run()