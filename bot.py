import requests
from bs4 import BeautifulSoup
import re

# Configuración del dominio activo de MadPlay77
BASE_URL = "https://ganzqowo.ps34buy87z6lothrough.sbs"
AGENDA_URL = f"{BASE_URL}/es/"

def capturar_partidos():
    # Usamos un User-Agent para que la web no nos bloquee
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    try:
        response = requests.get(AGENDA_URL, headers=headers, timeout=15)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', href=True)
            
            partidos = []
            for l in links:
                h = l['href']
                # Buscamos los IDs de 7 dígitos en fútbol y basket
                if re.search(r'(\d{7})', h) and any(s in h for s in ['basketball', 'football']):
                    # Armamos el link con la llave maestra icg=UFk
                    full_link = f"{BASE_URL}{h}?icg=UFk"
                    name = h.split('/')[-1].replace('.html', '').replace('-', ' ').title()
                    partidos.append(f"{name}|{full_link}")

            if partidos:
                # Escribimos el archivo que lee tu App de Sketchware
                with open("lista_canales.txt", "w") as f:
                    f.write("\n".join(partidos))
                print(f"Éxito: {len(partidos)} partidos capturados.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    capturar_partidos()
    
