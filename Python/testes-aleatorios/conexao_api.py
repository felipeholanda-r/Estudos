import requests
import socket
import whois
import speedtest
import json
import nmap
import ipaddress
import netifaces
from flask import Flask, jsonify

# O que foi importado para o projeto:
# pip install speedtest-cli requests python-whois flask  gunicorn netifaces ipaddress

app = Flask(__name__)
app.json.sort_keys = False

def obter_ip_publico():
    response = requests.get('https://api.ipify.org?format=json')
    data = response.json()
    ip = data['ip']
    return ip

def obter_provedor_internet(ip):
    w = whois.whois(ip)
    provider = w.registrant_name
    return provider

def testar_dowload():
    # Cria um objeto Speedtest
    st = speedtest.Speedtest()

    # Convertendo para megabits por segundo
    download_speed = st.download() / 1024 / 1024

    return round(download_speed)

def testar_upload():
    # Cria um objeto Speedtest
    st = speedtest.Speedtest()

    # Convertendo para megabits por segundo
    upload_speed = st.upload() / 1024 / 1024

    return round(upload_speed, 2)

def buscar_dispositivos_conectados(rede_cidr):
    nm = nmap.PortScanner()
    nm.scan(hosts=rede_cidr, arguments='-sn')

    dispositivos = []
    for host in nm.all_hosts():
        if 'mac' in nm[host]['addresses']:
            ip_address = nm[host]['addresses']['ipv4']
            mac_address = nm[host]['addresses']['mac']
            if nm[host]['vendor']:
                vendor = nm[host]['vendor'][mac_address]
            else:
                vendor = ''
            
            dispositivo={"ip":ip_address, "mac": mac_address, "fabricante":vendor}
            
            dispositivos.append(dispositivo)

    return dispositivos

def busca_rede(ip_address, netmask):
    endereco_ip = ip_address
    mascara_subrede = netmask

    rede_cidr = ipaddress.IPv4Network(f'{endereco_ip}/{mascara_subrede}', strict=False).with_prefixlen

    return rede_cidr

def obter_ip_local():
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        if interface != 'lo':
            enderecos = netifaces.ifaddresses(interface).get(netifaces.AF_INET)
            if enderecos:
                for endereco in enderecos:
                    ip = endereco['addr']
                    mascara = endereco['netmask']
                    return ip, mascara


@app.route('/api/v1/host-info', methods=['GET'])
def host_info():
    host = socket.gethostname()
    ip_local = socket.gethostbyname(host)
    dados = {
        'host' : host,
        'ip_local': ip_local
    }
    
    return jsonify(dados)

@app.route('/api/v1/connection-info', methods=['GET'])
def connection_info():
    ip_publico = obter_ip_publico()
    provedor_internet = obter_provedor_internet(ip_publico)

    dados = {
        'ip_publico' : ip_publico,
        'provedor' : provedor_internet
    }
    
    return jsonify(dados)

@app.route('/api/v1/speed-info', methods=['GET'])
def speed_info():
    download = testar_dowload()
    upload = testar_upload()

    dados = {
        'download' : download,
        'upload' : upload
    }
    
    return jsonify(dados)

@app.route('/api/v1/network-info', methods=['GET'])
def network_info():
    # Obtém o IP local e a máscara de rede
    ip_local, mascara_rede = obter_ip_local()

    #Obter ip e mascara no padrão CIDR
    rede_cidr = busca_rede(ip_local, mascara_rede)

    dispositivos_conectados = buscar_dispositivos_conectados(rede_cidr)
    return jsonify(dispositivos_conectados)

if __name__ == '__main__':
    app.run(port=3000)