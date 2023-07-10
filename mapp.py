from flask import Flask, request
import smtplib

app = Flask(__name__)

@app.route('/')
def index():
    ip = request.remote_addr

    # Configuração do servidor de email
    email_server = 'smtp.mail.yahoo.com'
    email_port = 465
    email_sender = 'minadoooo11@yahoo.com'
    email_password = 'prosopopei4'
    email_recipient = 'minadoooo11@yahoo.com'

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
        return f'Erro ao enviar o email: {str(e)}'

    return '', 204

if __name__ == '__main__':
    app.run()
