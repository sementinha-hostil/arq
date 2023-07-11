from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/salvar-ip', methods=['POST'])
def salvar_ip():
    ip = request.json['ip']
    caminho_arquivo = '/storage/emulated/0/db/ips.txt'
    with open(caminho_arquivo, 'a') as arquivo:
        arquivo.write(ip + '\n')
    return '', 200

if __name__ == '__main__':
    app.run()
