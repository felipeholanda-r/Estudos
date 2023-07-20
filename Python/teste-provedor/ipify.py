import requests
import socket

def obter_ip_publico():
    # Faz uma requisição para um serviço de obtenção do IP público
    response = requests.get('https://api.ipify.org/?format=json')
    ip = response.json()['ip']
    return ip

def obter_provedor_internet():
    # Obtém o nome do host local
    host = socket.gethostname()
    # Obtém o endereço IP local
    ip = socket.gethostbyname(host)
    # Obtém o provedor de internet usando o endereço IP local
    provedor = socket.gethostbyaddr(ip)[0]
    return provedor

if __name__ == '__main__':
    ip_publico = obter_ip_publico()
    provedor_internet = obter_provedor_internet()

    print(f"Endereço IP público: {ip_publico}")
    print(f"Provedor de internet: {provedor_internet}")
