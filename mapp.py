from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get-ip', methods=['GET'])
def get_ip():
    ip = request.headers.get('X-Real-IP', request.remote_addr)

    # Número de telefone para o qual deseja enviar a mensagem via WhatsApp
    numero_whatsapp = '5527996395105'

    # URL do WhatsApp API para enviar a mensagem
    url_whatsapp = f'https://api.whatsapp.com/send?phone={numero_whatsapp}&text='

    # Redireciona o usuário para o WhatsApp
    return jsonify({'redirect': url_whatsapp})

if __name__ == '__main__':
    app.run()
