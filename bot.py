import requests
import re
from concurrent.futures import ThreadPoolExecutor

# --- FUENTES DE ALTO RENDIMIENTO (60 FPS / 720p) ---
FUENTES_FLUIDAS = [
    "https://raw.githubusercontent.com/DeXTeR085/IPTV/main/Global.m3u",
    "https://raw.githubusercontent.com/m3u8playlist/free-iptv-channels/main/sport.m3u",
    "https://raw.githubusercontent.com/Soky9/TV/main/Sport.m3u",
    "https://iptv-org.github.io/iptv/index.m3u"
]

# --- OBJETIVOS DE FÚTBOL REAL ---
CANALES_FUTBOL = [
    "TIGO SPORTS", "TYC SPORTS", "ESPN", "FOX SPORTS", "WIN SPORTS", 
    "TNT SPORTS", "DIRECTV SPORTS", "DSPORTS", "GOLTV", "BEIN SPORTS",
    "MOVISTAR LALIGA", "DAZN", "SKY SPORTS", "PREMIER LEAGUE", "TUDN"
]

def capturar_fluidez(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    try:
        r = requests.get(url, headers=headers, timeout=20)
        # Captura Nombre y URL
        matches = re.findall(r'#EXTINF:.*?,(.*?)\n(http.*?m3u8[^\s]*)', r.text)
        
        botin_paso = []
        for nombre, link in matches:
            n_up = nombre.upper()
            l_low = link.lower()
            
            # 1. Filtro de Nombre (Solo fútbol)
            if any(f in n_up for f in CANALES_FUTBOL):
                # 2. Filtro de Basura (Fuera cine y novelas)
                if not any(b in n_up for b in ["CINE", "MOVIES", "RADIO", "KIDS", "NOVELA"]):
                    # 3. Filtro de Rendimiento (Buscamos 720 o señales estables)
                    # No obligamos a que diga HD, pero evitamos las que digan 360 o 240
                    if not any(q in n_up for q in ["360P", "240P", "LOW", "SD"]):
                        botin_paso.append(f"{nombre.strip()}|{link.strip()}")
        return botin_paso
    except:
        return []

def asalto_720_fps():
    print("🚀 Iniciando captura de señales fluidas (720p/FPS)...")
    total_recolectado = []

    with ThreadPoolExecutor(max_workers=8) as executor:
        listas = list(executor.map(capturar_fluidez, FUENTES_FLUIDAS))
    
    for l in listas:
        total_recolectado.extend(l)

    # Limpieza de duplicados
    botin_final = list(set(total_recolectado))

    with open("lista_canales.txt", "w", encoding='utf-8') as f:
        if botin_final:
            f.write("\n".join(botin_final))
            print(f"🏁 ¡ESTAMOS LISTOS! {len(botin_final)} canales capturados para su App.")
        else:
            f.write("ERROR|No se encontraron señales con la
                               
