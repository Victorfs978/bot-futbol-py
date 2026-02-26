import requests
from bs4 import BeautifulSoup
import re

# 1. Configuración del Objetivo (Dominio activo de MadPlay77)
BASE_URL = "https://ganzqowo.ps34buy87z6lothrough.sbs"
AGENDA_URL = f"{BASE_URL}/es/"

def capturar_partidos():
    print(f"[*] Iniciando extracción en: {AGENDA_URL}")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(AGENDA_URL, headers=headers, timeout=15)
        if response.status_code != 200:
            print(f"[-] Error de conexión: {response.status_code}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        
        lista_final = []
        
        # 2. Escaneo de IDs de 7 dígitos (Fútbol, Basket, etc.)
        for link in links:
            href = link['href']
            # Buscamos el patrón del deporte + el ID numérico
            if any(deporte in href for deporte in ['basketball', 'football', 'tennis']):
                match = re.search(r'(\d{7})', href)
                if match:
                    # Construimos el link con la llave maestra icg=UFk
                    url_directa = f"{BASE_URL}{href}?icg=UFk"
                    # Limpiamos el nombre para que se vea bien en tu App
                    nombre = href.split('/')[-1].replace('.html', '').replace('-', ' ').title()
                    lista_final.append(f"{nombre}|{url_directa}")

        # 3. Guardar en el archivo que lee tu App
        if lista_final:
            with open("lista_canales.txt", "w") as f:
                f.write("\n".join(lista_final))
            print(f"[!] Éxito: {len(lista_final)} partidos guardados en lista_canales.txt")
        else:
            print("[-] No se encontraron partidos hoy.")

    except Exception as e:
        print(f"[-] Error crítico: {e}")

if __name__ == "__main__":
    capturar_partidos()
    
