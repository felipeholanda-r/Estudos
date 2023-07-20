import speedtest

def testar_velocidade():
    # Cria um objeto Speedtest
    st = speedtest.Speedtest()
    
    print("Testando velocidade de download...")
    download_speed = st.download() / 1024 / 1024  # Convertendo para megabits por segundo
    print(f"Velocidade de download: {download_speed:.2f} Mbps")
    
    print("Testando velocidade de upload...")
    upload_speed = st.upload() / 1024 / 1024  # Convertendo para megabits por segundo
    print(f"Velocidade de upload: {upload_speed:.2f} Mbps")

def teste_dowload():
    # Cria um objeto Speedtest
    st.speedtest.Speedtest()

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
    teste_upload()
