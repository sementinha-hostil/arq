from flask import Flask, request
import os
import pymongo 

app = Flask(__name__)


@app.route('/salvar-ip', methods=['POST'])
def salvar_ip():
    ip = request.json['ip']
    
# Cria um cliente para o banco de dados
    client = pymongo.MongoClient()

# Cria o banco de dados
    db = client.create_database("my_database")

# Cria uma coleção no banco de dados
    collection = db.create_collection("my_collection")

# Insere um documento na coleção
    document = {"ip": ip}
    collection.insert_one(document)


if __name__ == '__main__':
    app.run()
