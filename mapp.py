from flask import Flask, request
import os
import smtplib

app = Flask(__name__)


@app.route('/salvar-ip', methods=['POST'])
def salvar_ip():
    ip = request.json['ip']
# Create an SMTP object
    smtp = smtplib.SMTP('smtp.gmail.com', 587)

# Set the SMTP server, username, and password
    smtp.ehlo()
    smtp.starttls()
    smtp.login('m4ria.gama@gmail.com', 'Prosopopei4')

# Set the sender and recipient
    sender = 'm4ria.gama@gmail.com'
    recipient = 'm4ria.gama@gmail.com'

# Set the email subject
    subject = 'ta aqui'

# Set the email body
    body = ip

# Send the email
    smtp.sendmail(sender, recipient, subject, body)

# Close the connection
    smtp.quit()


if __name__ == '__main__':
    app.run()
