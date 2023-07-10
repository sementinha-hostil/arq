import yagmail
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

    # Enviar o e-mail usando yagmail
    yag = yagmail.SMTP(remetente, senha)
    yag.send(to=destinatario, subject=assunto, contents=corpo_email)

    print('E-mail enviado com sucesso')

enviar_email()
