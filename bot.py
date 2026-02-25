import requests
import re
from concurrent.futures import ThreadPoolExecutor

# FUENTES AGREGADORAS (Repositorios de canales deportivos globales)
FUENTES_M3U = [
    "https://iptv-org.github.io/iptv/categories/sports.m3u",
    "https://raw.githubusercontent.com/Guiffre/IPTV-All-The-World/master/Sport.m3u",
    "https://raw.githubusercontent.com/m3u8playlist/free-iptv-channels/main/sport.m3u"
]

# WEBS QUE CENTRALIZAN AGENDAS (Para sacar el fútbol del día)
SITIOS_CENTRALES = [
    "https://verliga.live",
    "https://futbollibre.net.ar",
    "https://Rojadirecta.me",
    "https://pirlo.tv"
]

def extraer_lista_global(url):
    try:
        r = requests.get(url, timeout=15)
        # Buscamos patrones de canales: Nombre y URL
        canales = re.findall(r'#EXTINF:.*?,(.*?)\n(http.*?m3u8)', r.text)
        return [f"{c[0].strip()}|{c[1].strip()}" for c in canales]
    except:
        return []

def extraer_web_central(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/122.0.0.0'}
    try:
        r = requests.get(url, headers=headers, timeout=15)
        # Buscamos iframes o links directos que ya estén públicos
        links = re.findall(r'https?://[^\s\'"]+\.(?:m3u8|php\?id=\d+)', r.text)
        return [f"EVENTO_VIVO|{l}" for l in set(links)]
    except:
        return []

def asalto_mundial():
    print("🌍 Iniciando captura de canales deportivos mundiales...")
    botin_total = []

    # 1. Atacar Repositorios M3U (Canales fijos: ESPN, Fox, TyC, BeIN, etc.)
    with ThreadPoolExecutor(max_workers=5) as executor:
        listas = list(executor.map(extraer_lista_global, FUENTES_M3U))
        for lista in listas:
            botin_total.extend(lista)

    # 2. Atacar Agendas (Partidos del momento)
    with ThreadPoolExecutor(max_workers=5) as executor:
        agendas = list(executor.map(extraer_web_central, SITIOS_CENTRALES))
        for agenda in agendas:
            botin_total.extend(agenda)

    # Filtrar duplicados y limpiar nombres
    botin_limpio = list(set(botin_total))

    # Escribir el archivo final para Sketchware
    with open("lista_canales.txt", "w", encoding='utf-8') as f:
        if botin_limpio:
            f.write("\n".join(botin_limpio[:500])) # Limitamos a los mejores 500
            print(f"✅ ¡ÉXITO! {len(botin_limpio)} canales mundiales capturados.")
        else:
            f.write("ERROR|Sin señales disponibles")

if __name__ == "__main__":
    asalto_mundial()
    
