import requests
import re
from concurrent.futures import ThreadPoolExecutor

# --- EL RADAR DE ÉLITE: SOLO NOMBRES DE FÚTBOL ---
NOMBRES_OBJETIVO = [
    # Sudamérica & Centro
    "Tigo Sports", "TyC Sports", "TNT Sports", "DSports", "GolTV", "Win Sports", 
    "ESPN", "Fox Sports", "VIX", "TUDN", "Claro Sports", "TV Max", "RPC Deportes",
    # Europa & Internacional
    "beIN Sports", "DAZN", "Movistar Liga", "Sky Sports", "BT Sport", "Eurosport", 
    "LaLiga TV", "Premier League TV", "RMC Sport", "Canal+ Sport", "Eleven Sports",
    # Canales de Clubes y Ligas
    "Barca TV", "Real Madrid TV", "MUTV", "Milan TV", "FIFA+", "UEFA TV"
]

FUENTES_IPTV = [
    "https://iptv-org.github.io/iptv/index.m3u",
    "https://raw.githubusercontent.com/iptv-org/iptv/master/categories/sports.m3u",
    "https://raw.githubusercontent.com/Fmacedo87/iptv/master/Deportes.m3u"
]

def filtrar_por_nombre(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=headers, timeout=30)
        # Captura: #EXTINF:...,Nombre del Canal \n URL
        matches = re.findall(r'#EXTINF:.*?,(.*?)\n(http.*?m3u8[^\s]*)', r.text)
        
        resultados = []
        for nombre, link in matches:
            nombre_up = nombre.upper()
            # Verificamos si el canal está en nuestra lista de ÉLITE
            if any(n.upper() in nombre_up for n in NOMBRES_OBJETIVO):
                # Filtro de seguridad: nada de "Cine", "Radio" o "Adultos"
                if not any(b in nombre_up for b in ["CINE", "RADIO", "XXX", "MOVIES", "KIDS"]):
                    resultados.append(f"{nombre.strip()}|{link.strip()}")
        return resultados
    except:
        return []

def ejecucion_asalto_global():
    print("📡 Iniciando barrido mundial de canales de fútbol...")
    botin_final = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        listas_capturadas = list(executor.map(filtrar_por_nombre, FUENTES_IPTV))
    
    for lista in listas_capturadas:
        botin_final.extend(lista)

    # Limpiamos duplicados y ordenamos
    botin_final = sorted(list(set(botin_final)))

    with open("lista_canales.txt", "w", encoding='utf-8') as f:
        if botin_final:
            f.write("\n".join(botin_final))
            print(f"🏁 ¡MISIÓN CUMPLIDA! Se capturaron {len(botin_final)} canales de fútbol.")
        else:
            f.write("ERROR|No se encontraron los canales con esos nombres.")

if __name__ == "__main__":
    ejecucion_asalto_global()
    
