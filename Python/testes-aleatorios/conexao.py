import requests
import socket
import whois
import speedtest
import json
import nmap
import ipaddress
import netifaces


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

# Função para obter a lista de dispositivos conectados na rede com IP, MAC e Fabricante
def informacoes_rede(rede_cidr):
    nm = nmap.PortScanner()
    nm.scan(hosts=rede_cidr, arguments='-sn')
    result = nm.analyse_nmap_xml_scan()
    
    scan = {'uphosts': int(result['nmap']['scanstats']['uphosts']), 
            'downhosts': int(result['nmap']['scanstats']['downhosts']), 
            'totalhosts': int(result['nmap']['scanstats']['totalhosts'])}

    return scan

# Função para obter o IP e máscara de rede no padrão CIDR (0.0.0.0/0)
def busca_rede(ip_address, netmask):
    endereco_ip = ip_address
    mascara_subrede = netmask

    rede_cidr = ipaddress.IPv4Network(f'{endereco_ip}/{mascara_subrede}', strict=False).with_prefixlen

    return rede_cidr

# Função para obter o IP da rede local e a máscara de rede
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

if __name__ == '__main__':
    # Obtém o IP local e a máscara de rede
    ip_local, mascara_rede = obter_ip_local()

    #Obter ip e mascara no padrão CIDR
    rede_cidr = busca_rede(ip_local, mascara_rede)

    dispositivos_conectados = buscar_dispositivos_conectados(rede_cidr)

    print(json.dumps(dispositivos_conectados))