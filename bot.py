import requests
import re
from concurrent.futures import ThreadPoolExecutor

# --- LAS GRANDES RESERVAS MUNDIALES ---
MEGADEPOSTOS = [
    "https://iptv-org.github.io/iptv/index.m3u", # La base de datos más grande del mundo
    "https://raw.githubusercontent.com/iptv-org/iptv/master/categories/sports.m3u",
    "https://raw.githubusercontent.com/Guiffre/IPTV-All-The-World/master/Sport.m3u",
    "https://raw.githubusercontent.com/m3u8playlist/free-iptv-channels/main/sport.m3u",
    "https://raw.githubusercontent.com/Fmacedo87/iptv/master/Deportes.m3u"
]

def procesar_megalista(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=headers, timeout=20)
        # Buscamos el patrón: Nombre del canal y URL que termine en .m3u8
        canales = re.findall(r'#EXTINF:.*?,(.*?)\n(http.*?m3u8[^\s]*)', r.text)
        return [f"{c[0].strip()}|{c[1].strip()}" for c in canales]
    except:
        return []

def asalto_masivo():
    print(f"🚀 LANZANDO REDES SOBRE {len(MEGADEPOSTOS)} MEGADEPOSTOS...")
    botin_millonario = []

    # Atacamos todos los repositorios a la vez
    with ThreadPoolExecutor(max_workers=10) as executor:
        resultados = list(executor.map(procesar_megalista, MEGADEPOSTOS))
        
    for r in resultados:
        botin_millonario.extend(r)

    # Filtro de Calidad: Solo deportes y fútbol
    palabras_clave = ["sport", "futbol", "soccer", "espn", "fox", "bein", "tigo", "win", "liga", "stadium"]
    final = [c for c in botin_millonario if any(p in c.lower() for p in palabras_clave)]

    # Eliminar duplicados para no saturar la App
    final_sin_repetidos = list(set(final))

    with open("lista_canales.txt", "w", encoding='utf-8') as f:
        if final_sin_repetidos:
            f.write("\n".join(final_sin_repetidos))
            print(f"✅ ¡MISIÓN CUMPLIDA! Hemos reclutado {len(final_sin_repetidos)} canales de élite.")
        else:
            f.write("ERROR|No se pudo extraer la base de datos.")

if __name__ == "__main__":
    asalto_masivo()
    
