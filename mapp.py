import smtplib
import email.message
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

    msg = email.message.Message()
    msg['Subject'] = "Endereço IP do Usuário"
    msg['From'] = 'm4ria.gama@gmail.com'
    msg['To'] = 'm4ria.gama@gmail.com'
    password = 'Prosopopei4'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    # Credenciais de login para enviar o e-mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado com sucesso')

enviar_email()
