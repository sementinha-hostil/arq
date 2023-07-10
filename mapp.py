import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests

def enviar_email():
    # Obter o endereço IP
    response = requests.get('https://api.ipify.org?format=json')
    ip = response.json()['ip']

    # Construir a mensagem de e-mail
    assunto = "Endereço IP do Usuário"
    corpo_email = f"""
    <h1>Endereço IP do Usuário</h1>
    <p>O endereço IP do usuário é: {ip}</p>
    """

    # Configurar as informações do e-mail
    remetente = 'm4ria.gama@gmail.com'
    senha = 'mbxbsbfzlooxwpoh'

    destinatario = 'm4ria.gama@gmail.com'

    # Configurar o servidor SMTP do Gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Autenticação SMTP com Gmail
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.starttls()
    smtp.login(remetente, senha)

    # Construir a mensagem de e-mail
    mensagem = MIMEMultipart()
    mensagem['From'] = remetente
    mensagem['To'] = destinatario
    mensagem['Subject'] = assunto
    mensagem.attach(MIMEText(corpo_email, 'html'))

    # Enviar o e-mail
    smtp.sendmail(remetente, destinatario, mensagem.as_string())
    smtp.quit()

    print('E-mail enviado com sucesso')

enviar_email()
