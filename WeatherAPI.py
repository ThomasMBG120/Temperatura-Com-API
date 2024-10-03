import requests
import time

# Sua chave de API da WeatherAPI
API_KEY = 'sua_chave_da_weatherapi'

# Função para obter o endereço IP público
def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()
        ip_data = response.json()
        return ip_data['ip']
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter o endereço IP: {e}")
        return None

# Função para obter as condições do tempo baseado no IP
def get_weather_by_ip(api_key, ip_address):
    try:
        url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={ip_address}'
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter as condições do tempo: {e}")
        return None

# Função principal que executa a cada 30 segundos
def main():
    ip_address = get_public_ip()
    if not ip_address:
        print("Não foi possível obter o endereço IP.")
        return
    
    while True:
        weather_data = get_weather_by_ip(API_KEY, ip_address)
        if weather_data:
            location = weather_data['location']['name']
            region = weather_data['location']['region']
            country = weather_data['location']['country']
            condition = weather_data['current']['condition']['text']
            temp_c = weather_data['current']['temp_c']
            
            print(f"Localização: {location}, {region}, {country}")
            print(f"Condição atual: {condition}")
            print(f"Temperatura: {temp_c}°C")
            print("-" * 40)
        else:
            print("Erro ao obter as condições do tempo.")

        time.sleep(30)  # Aguarda 30 segundos antes de atualizar novamente

if __name__ == "__main__":
    main()
