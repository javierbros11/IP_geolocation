# External Packages
import ipinfo
import folium
from dotenv import load_dotenv

# Local Packages
import os
import sys


# Configuración
load_dotenv() # <- Introducir previamente el token de acceso de ipinfo
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

def get_ip_details(ip,access_token):
    """
    Obtiene detalles de geolocalización de una IP usando ipinfo.

    Args:
        ip(str): IP que se desea geolocalizar.
        access_token(str): Token de acceso de la cuenta de ipinfo.
    """

    try:
        handler = ipinfo.getHandler(access_token) # Definimos el cliente
        details = handler.getDetails(ip) # Obtenemos la info de la IP
        return details.all
    
    except Exception as e:
        print(f"Error al obtener los detalles de la IP: {ip}")
        sys.exit(1)

def draw_map(latitude,longitude,location,filename="map.html"):
    """
    Dibuja un mapa basándose en los detalles de geolocalización de una ip.

    Args:
        latitude(str): Latitud.
        longitude(str): Longitud.
        location(str): Localización.
        filename(str): Nombre del archivo donde se almacenará el mapa.
    """

    my_map = folium.Map(location=[latitude,longitude], zoom_start=9)
    folium.Marker([latitude,longitude], popup=location).add_to(my_map)
    my_map.save(filename)

    return os.path.abspath(filename)

# Inicio del programa

if __name__ == "__main__":
    
    ip_address = input("Dime una dirección IPv4: ")
    details = get_ip_details(ip_address,ACCESS_TOKEN)

    # Mostramos los detalles de la IP por pantalla

    for key,value in details.items():
        print(f"{key} : {value}")

    # Obtenemos los valores de latitud,longitud y localización
    
    latitude = details["latitude"]
    longitude = details["longitude"]
    location = details.get("region", "Ubicación desconocida")

    map_file_path = draw_map(latitude,longitude,location)
    print(f"Mapa guardado en: {map_file_path}")