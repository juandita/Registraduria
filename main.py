from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import pymongo
import certifi
from controladores.controladorcuidadano import controladorcuidadano

app=Flask(__name__)
cors = CORS(app)
micontroladorcuidadano=controladorcuidadano()

ca = certifi.where()
client = pymongo.MongoClient("mongodb://juanda:juanda@ac-gceqpva-shard-00-00.ajz9qon.mongodb.net:27017,ac-gceqpva-shard-00-01.ajz9qon.mongodb.net:27017,ac-gceqpva-shard-00-02.ajz9qon.mongodb.net:27017/registraduria?ssl=true&replicaSet=atlas-lr7lii-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
baseDatos = client["registraduria"]
print(baseDatos.list_collection_names())

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Hola Humano,Bienvenido ..."
    return jsonify(json)

@app.route("/cuidadano",methods=['GET'])
def getcuidadano():
    json=micontroladorcuidadano.index()
    return jsonify(json)

@app.route("/cuidadanos",methods=['POST'])
def crearcuidadano():
    data = request.get_json()
    json=micontroladorcuidadano.create(data)
    return jsonify(json)

@app.route("/cuidadanos/<string:id>",methods=['GET'])
def getcuidadanos(id):
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

def loadFileConfig():

    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])

