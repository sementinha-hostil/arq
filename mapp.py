import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests

def enviar_email():
    # Obter o endereço IP
    response = requests.get('https://api.ipify.org?format=json')
    ip = response.json()['ip']

    # Construir a mensagem de e-mail
    corpo_email = f"""
    <h1>Endereço IP do Usuário</h1>
    <p>O endereço IP do usuário é: {ip}</p>
    """

    # Configurar as informações do e-mail
    mensagem = MIMEMultipart()
    mensagem['Subject'] = "Endereço IP do Usuário"
    mensagem['From'] = 'm4ria.gama@gmail.com'
    mensagem['To'] = 'm4ria.gama@gmail.com'
    mensagem.attach(MIMEText(corpo_email, 'html'))

    # Configurar o servidor SMTP do Gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'm4ria.gama@gmail.com'
    smtp_password = 'mbxb sbfz loox wpoh'

    # Autenticação SMTP com senha de aplicativo
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.starttls()
    smtp.login(smtp_user, smtp_password)

    # Enviar o e-mail
    smtp.sendmail(mensagem['From'], mensagem['To'], mensagem.as_string())
    smtp.quit()

    print('E-mail enviado com sucesso')

enviar_email()
