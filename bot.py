import requests
import re
from concurrent.futures import ThreadPoolExecutor

# --- FUENTES DE DEPORTES MASIVAS (TODO LO QUE SEA DEPORTE) ---
FUENTES_DEPORTES = [
    "https://raw.githubusercontent.com/iptv-org/iptv/master/categories/sports.m3u",
    "https://raw.githubusercontent.com/Fmacedo87/iptv/master/Deportes.m3u",
    "https://raw.githubusercontent.com/m3u8playlist/free-iptv-channels/main/sport.m3u",
    "https://raw.githubusercontent.com/Soky9/TV/main/Sport.m3u",
    "https://raw.githubusercontent.com/Guiffre/IPTV-All-The-World/master/Sport.m3u"
]

def captura_bruta(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=headers, timeout=30)
        # Captura cualquier cosa que tenga el formato #EXTINF seguido de un link http
        # Esto ignora nombres y captura todo lo que el archivo diga que es TV
        matches = re.findall(r'#EXTINF:.*?,(.*?)\n(http.*?m3u8[^\s]*)', r.text)
        
        return [f"{c[0].strip()}|{c[1].strip()}" for c in matches]
    except:
        return []

def ataque_total_sin_filtros():
    print("🧨 LANZANDO ATAQUE BRUTO... CAPTURANDO TODO EL DEPORTE MUNDIAL.")
    botin_masivo = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        resultados = list(executor.map(captura_bruta, FUENTES_DEPORTES))
    
    for r in resultados:
        botin_masivo.extend(r)

    # Solo quitamos los repetidos para no llenar la App de basura igual
    botin_final = list(set(botin_masivo))

    with open("lista_canales.txt", "w", encoding='utf-8') as f:
        if botin_final:
            f.write("\n".join(botin_final))
            print(f"🏁 ASALTO COMPLETADO: {len(botin_final)} canales capturados sin filtros.")
        else:
            f.write("ERROR|No se pudo extraer nada de las fuentes.")

if __name__ == "__main__":
    ataque_total_sin_filtros()
    
