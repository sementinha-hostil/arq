from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import requests
import datetime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(String, primary_key=True)
    ip = Column(String)
    data_adicao = Column(DateTime)

def salvar_ip_no_banco(ip):
    engine = create_engine('sqlite:////storage/emulated/0/db/projetineo.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    usuario = Usuario(id='1', ip=ip, data_adicao=datetime.datetime.now())
    session.add(usuario)
    session.commit()
    session.close()

def obter_ip():
    response = requests.get('https://api.ipify.org?format=json')
    ip = response.json()['ip']
    return ip

def main():
    ip = obter_ip()
    salvar_ip_no_banco(ip)
    print('IP salvo no banco de dados com sucesso.')

if __name__ == '__main__':
    main()
