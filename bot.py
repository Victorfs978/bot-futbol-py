import urllib.request
import re

# Configuración del dominio activo
BASE_URL = "https://ganzqowo.ps34buy87z6lothrough.sbs"
AGENDA_URL = f"{BASE_URL}/es/"

def capturar_partidos():
    print(f"[*] Extrayendo de: {AGENDA_URL}")
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        req = urllib.request.Request(AGENDA_URL, headers=headers)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            
            # Buscamos los IDs de 7 dígitos directamente en el código
            # Formato: /deporte/liga-ID/partido.html
            patron = r'href="([^"]+/(?:basketball|football|tennis)/[^"]+(\d{7})/[^"]+\.html)"'
            enlaces = re.findall(patron, html)
            
            partidos = []
            for href, id_partido in enlaces:
                # Armamos el link con la llave maestra icg=UFk
                full_link = f"{BASE_URL}{href}?icg=UFk"
                # Limpiamos el nombre del partido
                name = href.split('/')[-1].replace('.html', '').replace('-', ' ').title()
                partidos.append(f"{name}|{full_link}")

            # Guardamos el archivo que lee tu App
            if partidos:
                # Eliminamos duplicados
                partidos = list(set(partidos))
                with open("lista_canales.txt", "w") as f:
                    f.write("\n".join(partidos))
                print(f"¡Éxito! {len(partidos)} partidos capturados.")
            else:
                print("No se encontraron partidos.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    capturar_partidos()
    
