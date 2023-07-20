import nmap
import json
import ipaddress
import netifaces

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
            #info ={"mac": mac_address, "fabricante":vendor}
            dispositivo={"ip":ip_address, "mac": mac_address, "fabricante":vendor}

            
            dispositivos.append(dispositivo)

            #dispositivos.append(ip_address, [mac_address, ip_address, vendor])

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



if __name__ == '__main__':
    # Obtém o IP local e a máscara de rede
    ip_local, mascara_rede = obter_ip_local()

    rede_cidr = busca_rede(ip_local, mascara_rede)

    dispositivos_conectados = buscar_dispositivos_conectados(rede_cidr)
    dados_json = json.dumps(dispositivos_conectados, indent=4)
    print(dados_json)