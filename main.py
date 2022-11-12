import certifi
import pymongo
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from controladores.controladorcuidadano import controladorcuidadano
from controladores.controladorcandidato import controladorcandidato
from controladores.controladormesa import controladormesa
from controladores.controladorpartidopolitico import controladorpartidopolitico
from controladores.controladorvoto_candidato import controladorvotocandidato
from controladores.controladorvoto_partido_politico import controladorvotoPP
app=Flask(__name__)
cors = CORS(app)

micontroladorcuidadano=controladorcuidadano()
micontroladorcandidato=controladorcandidato()
micontroladormesa=controladormesa()
micontroladorpartidopolitico=controladorpartidopolitico()
micontorladorvotocandidato=controladorvotocandidato()
micontroladorvotopartidopolitico=controladorvotoPP()

ca = certifi.where()
client = pymongo.MongoClient("mongodb://juanda:juanda@ac-gceqpva-shard-00-00.ajz9qon.mongodb.net:27017,ac-gceqpva-shard-00-01.ajz9qon.mongodb.net:27017,ac-gceqpva-shard-00-02.ajz9qon.mongodb.net:27017/registraduria?ssl=true&replicaSet=atlas-lr7lii-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
baseDatos = client["registraduria"]
print(baseDatos.list_collection_names())

def load_file_config():
  with open("config.json") as f:
    data = json.load(f)
  return data


@app.route("/",methods=['GET'])
def test():
    json = {"message": "Hola Humano,Bienvenido ..."}
    return jsonify(json)

@app.route("/cuidadano",methods=["GET"])
def listar_cuidadano():
    listar_cuidadano = micontroladorcuidadano.index()
    return jsonify(listar_cuidadano)

@app.route("/cuidadanos",methods=['POST'])
def crearcuidadano():
    data = request.get_json()
    json=micontroladorcuidadano.create(data)
    return jsonify(json)

@app.route("/cuidadanos/<string:id>",methods=['GET'])
def get2cuidadanos(id):
    json=micontroladorcuidadano.show(id)
    return jsonify(json)

@app.route("/cuidadanos/<string:id>",methods=['PUT'])
def modificarcuidadano(id):
    data = request.get_json()
    json=micontroladorcuidadano.update(id,data)
    return jsonify(json)

@app.route("/cuidadanos/<string:id>",methods=['DELETE'])
def eliminarcuidadano(id):
    json=micontroladorcuidadano.delete(id)
    return jsonify(json)

###########
#Candidato#
###########

@app.route("/candidato",methods=["GET"])
def listar_candidato():
    listar_candidato = micontroladorcandidato.index()
    return jsonify(listar_candidato)

@app.route("/candidatos",methods=['POST'])
def crearcandidato():
    data = request.get_json()
    json=micontroladorcandidato.create(data)
    return jsonify(json)

@app.route("/candidatos/<string:id>",methods=['GET'])
def getcandidato(id):
    json=micontroladorcandidato.show(id)
    return jsonify(json)

@app.route("/candidatos/<string:id>",methods=['PUT'])
def modificarcandidato(id):
    data = request.get_json()
    json=micontroladorcandidato.update(id,data)
    return jsonify(json)

@app.route("/candidatos/<string:id>",methods=['DELETE'])
def eliminarcandidato(id):
    json=micontroladorcandidato.delete(id)
    return jsonify(json)

######
#mesa#
######

@app.route("/mesa", methods=["GET"])
def listar_mesa():
    listar_mesa = micontroladormesa.index()
    return jsonify(listar_mesa)

@app.route("/mesas", methods=['POST'])
def crearmesa():
    data = request.get_json()
    json=micontroladormesa.create(data)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['GET'])
def getmesa(id):
    json=micontroladormesa.show(id)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['PUT'])
def modificarmesa(id):
    data = request.get_json()
    json=micontroladormesa.update(id,data)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['DELETE'])
def eliminarmesa(id):
    json=micontroladormesa.delete(id)
    return jsonify(json)


##################
#partido_politico#
##################

@app.route("/partidopolitico", methods=["GET"])
def listar_partidopolitico():
    listar_partidopolitico = micontroladorpartidopolitico.index()
    return jsonify(listar_partidopolitico)

@app.route("/partidopoliticos", methods=['POST'])
def crearpartidopolitico():
    data = request.get_json()
    json=micontroladorpartidopolitico.create(data)
    return jsonify(json)

@app.route("/partidopoliticos/<string:id>", methods=['GET'])
def getpartidopolitico(id):
    json=micontroladorpartidopolitico.show(id)
    return jsonify(json)

@app.route("/partidopoliticos/<string:id>", methods=['PUT'])
def modificarpartidopolitico(id):
    data = request.get_json()
    json=micontroladorpartidopolitico.update(id,data)
    return jsonify(json)

@app.route("/partidopoliticos/<string:id>", methods=['DELETE'])
def eliminarpartidopolitico(id):
    json=micontroladorpartidopolitico.delete(id)
    return jsonify(json)


#################
#votos candidato#
#################

@app.route("/votocandidato", methods=["GET"])
def listar_votocandidato():
  lista_votosC = micontorladorvotocandidato.index()
  return jsonify(lista_votosC)

@app.route("/votocandidatos", methods=["POST"])
def crear_votocandidato():
  info_votosC = request.get_json()
  json = micontorladorvotocandidato.create(info_votosC)
  return jsonify(json)

@app.route("/votocandidatos/<string:id>", methods=['GET'])
def getvotocandidato(id):
    json=micontorladorvotocandidato.show(id)
    return jsonify(json)

@app.route("/votocandidatos/<string:id>", methods=['PUT'])
def modificarvotocandidato(id):
    data = request.get_json()
    json=micontorladorvotocandidato.update(id,data)
    return jsonify(json)

@app.route("/votocandidatos/<string:id>", methods=['DELETE'])
def eliminarvotocandidato(id):
    json=micontorladorvotocandidato.delete(id)
    return jsonify(json)

######################
#votopartidopolitico#
######################

@app.route("/votopp", methods=["GET"])
def listar_votopartidopolitico():
  lista_votoPP = micontroladorvotopartidopolitico.index()
  return jsonify(lista_votoPP)

@app.route("/votopps", methods=["POST"])
def crear_votopartidopolitico():
  info_votoPP = request.get_json()
  json = micontroladorvotopartidopolitico.create(info_votoPP)
  return jsonify(json)

@app.route("/votopps/<string:id>", methods=['GET'])
def getvotopartidopolitico(id):
    json=micontroladorvotopartidopolitico.show(id)
    return jsonify(json)

@app.route("/votopps/<string:id>", methods=['PUT'])
def modificarvotopartidopolitico(id):
    data = request.get_json()
    json=micontroladorvotopartidopolitico.update(id,data)
    return jsonify(json)

@app.route("/votopps/<string:id>", methods=['DELETE'])
def eliminarvotopartidopolitico(id):
    json=micontroladorvotopartidopolitico.delete(id)
    return jsonify(json)


if __name__=='__main__':
    dataConfig =load_file_config()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])

