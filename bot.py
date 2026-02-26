import urllib.request
import re
import os

# Configuración del dominio activo
BASE_URL = "https://ganzqowo.ps34buy87z6lothrough.sbs"
AGENDA_URL = f"{BASE_URL}/es/"

def capturar_partidos():
    print(f"[*] Atacando: {AGENDA_URL}")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    try:
        req = urllib.request.Request(AGENDA_URL, headers=headers)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            
            # Buscamos el patrón: /deporte/liga-ID/partido.html
            patron = r'href="([^"]+/(?:basketball|football|tennis)/[^"]+(\d{7})/[^"]+\.html)"'
            enlaces = re.findall(patron, html)
            
            partidos = []
            for href, id_partido in enlaces:
                # El link final con la llave maestra
                full_link = f"{BASE_URL}{href}?icg=UFk"
                name = href.split('/')[-1].replace('.html', '').replace('-', ' ').title()
                partidos.append(f"{name}|{full_link}")

            if partidos:
                # Guardamos para que Sketchware lo lea
                with open("lista_canales.txt", "w") as f:
                    f.write("\n".join(list(set(partidos))))
                print(f"¡Éxito! {len(partidos)} partidos capturados.")
            else:
                print("No se hallaron partidos. Verifica el dominio.")
    except Exception as e:
        print(f"Fallo en el ataque: {e}")

if __name__ == "__main__":
    capturar_partidos()
        
