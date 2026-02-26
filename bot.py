import requests
import re
from concurrent.futures import ThreadPoolExecutor

# --- LAS MEJORES FUENTES DE FÚTBOL GLOBAL ---
FUENTES_MUNDIALES = [
    "https://iptv-org.github.io/iptv/index.m3u",
    "https://raw.githubusercontent.com/iptv-org/iptv/master/categories/sports.m3u",
    "https://raw.githubusercontent.com/Fmacedo87/iptv/master/Deportes.m3u",
    "https://raw.githubusercontent.com/m3u8playlist/free-iptv-channels/main/sport.m3u"
]

def extraer_solo_futbol(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    # Diccionario de búsqueda: Solo términos de fútbol y ligas
    terminos_futbol = [
        "futbol", "soccer", "football", "liga", "cup", "champions", 
        "espn", "fox sports", "bein", "tigo sports", "win sports", 
        "tyc sports", "dsports", "goltv", "directv sports", "tnt sports",
        "laliga", "premier", "bundesliga", "serie a", "conmebol", "libertadores"
    ]
    # Lista de exclusión: Lo que NO queremos (Cine, Novelas, etc.)
    basura = ["cine", "movie", "novel", "kids", "infantil", "news", "noticias", "music", "radio"]
    
    try:
        r = requests.get(url, headers=headers, timeout=25)
        # Capturamos el nombre (#EXTINF) y el link (http)
        matches = re.findall(r'#EXTINF:.*?,(.*?)\n(http.*?m3u8[^\s]*)', r.text)
        
        filtrados = []
        for nombre, link in matches:
            nombre_clean = nombre.strip().lower()
            # 1. Debe tener una palabra de fútbol
            if any(p in nombre_clean for p in terminos_futbol):
                # 2. NO debe tener palabras de cine/novelas
                if not any(b in nombre_clean for b in basura):
                    filtrados.append(f"{nombre.strip()}|{link.strip()}")
        return filtrados
    except:
        return []

def asalto_futbol_total():
    print("⚽ INICIANDO FILTRADO MUNDIAL DE FÚTBOL...")
    botin_futbol = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        resultados = list(executor.map(extraer_solo_futbol, FUENTES_MUNDIALES))
    
    for r in resultados:
        botin_futbol.extend(r)

    # Eliminar repetidos y ordenar por nombre
    botin_final = sorted(list(set(botin_futbol)))

    with open("lista_canales.txt", "w", encoding='utf-8') as f:
        if botin_final:
            f.write("\n".join(botin_final))
            print(f"✅ ¡MISIÓN CUMPLIDA! {len(botin_final)} canales de FÚTBOL listos.")
        else:
            f.write("ERROR|No se encontraron señales de fútbol.")

if __name__ == "__main__":
    asalto_futbol_total()
    
