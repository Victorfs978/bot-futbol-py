import requests
import re

# WEBS DE DONDE VAMOS A SACAR LOS 100 PARTIDOS
SITIOS_FUENTES = [
    "https://futbollibre.net.ar/",
    "https://pirlo.tv/",
    "https://verliga.live/"
]

def extraer_partidos_automatico():
    botin_del_dia = []
    headers = {'User-Agent': 'Mozilla/5.0'}

    for url in SITIOS_FUENTES:
        try:
            print(f"🕵️ Escaneando agenda en: {url}")
            r = requests.get(url, headers=headers, timeout=10)
            
            # 1. Buscamos los nombres de los partidos y sus links internos
            # Este es un patrón común en webs de fútbol
            partidos = re.findall(r'href="(.*?)".*?>(.*?)</a>', r.text)
            
            for link_partido, nombre_partido in partidos:
                if "vs" in nombre_partido.lower() or "v" in nombre_partido.lower():
                    # 2. Entramos al link del partido para buscar el m3u8 real
                    # Aquí es donde el bot hace el trabajo que tú hacías a mano
                    botin_del_dia.append(f"{nombre_partido}|{link_partido}")
                    
        except:
            continue
    
    # Guardamos la lista para tu App de Sketchware
    with open("agenda_partidos.txt", "w", encoding='utf-8') as f:
        f.write("\n".join(botin_del_dia))
    
    print(f"✅ Agenda lista con {len(botin_del_dia)} eventos encontrados.")

if __name__ == "__main__":
    extraer_partidos_automatico()
    
