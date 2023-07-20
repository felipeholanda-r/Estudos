import requests
import whois

def obter_ip_publico():
    response = requests.get('https://api.ipify.org?format=json')
    data = response.json()
    ip = data['ip']
    return ip

def obter_provedor_internet(ip):
    w = whois.whois(ip)
    provider = w.registrant_name
    return provider

if __name__ == '__main__':
    ip_publico = obter_ip_publico()
    provedor_internet = obter_provedor_internet(ip_publico)
    
    print(f"Endereço IP público: {ip_publico}")
    print(f"Provedor de Internet: {provedor_internet}")
