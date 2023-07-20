import requests
import socket
import whois
import speedtest
import json


def obter_ip_publico():
    response = requests.get('https://api.ipify.org?format=json')
    data = response.json()
    ip = data['ip']
    return ip

def obter_provedor_internet(ip):
    w = whois.whois(ip)
    provider = w.registrant_name
    return provider

def teste_dowload():
    # Cria um objeto Speedtest
    st = speedtest.Speedtest()

    # Convertendo para megabits por segundo
    download_speed = st.download() / 1024 / 1024

    return round(download_speed)

def teste_upload():
    # Cria um objeto Speedtest
    st = speedtest.Speedtest()

    # Convertendo para megabits por segundo
    upload_speed = st.upload() / 1024 / 1024

    return round(upload_speed, 2)

if __name__ == '__main__':
    ip_publico = obter_ip_publico()
    provedor_internet = obter_provedor_internet(ip_publico)
    download = teste_dowload()
    upload = teste_upload()

    dados = {
        'ip_publico' : ip_publico,
        'provedor' : provedor_internet,
        'download' : download,
        'upload' : upload
        }
    
    dados_json = json.dumps(dados, indent=4)
    
    print(dados_json)