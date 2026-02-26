import requests
import re
from concurrent.futures import ThreadPoolExecutor

# --- EL RADAR DE NOMBRES: FÚTBOL MUNDIAL ---
NOMBRES_FUTBOL = [
    # Sudamérica y Centroamérica
    "Tigo Sports", "TyC Sports", "TNT Sports", "DSports", "DIRECTV Sports", 
    "Win Sports", "GolTV", "VIX", "TUDN", "Claro Sports", "TV Max", "RPC Deportes", 
    "Latina", "Caracol", "RCN", "Teleamazonas", "TV Publica", "Azteca Deportes",
    # Internacional y Europa
    "ESPN", "Fox Sports", "beIN Sports", "DAZN", "Movistar Liga", "Sky Sports", 
    "BT Sport", "Eurosport", "LaLiga TV", "Premier League", "RMC Sport", 
    "Canal+ Sport", "Eleven Sports", "Setanta Sports", "Ziggo Sport",
    # Canales de Clubes y FIFA
    "Real Madrid TV", "Barca TV", "MUTV", "Milan TV", "FIFA+", "UEFA TV"
]

FUENTES_MUNDIALES = [
    "https://iptv-org.github.io/iptv/index.m3u",
    "https://raw.githubusercontent.com/iptv-org/iptv/master/categories/sports.m3u",
    "https://raw.githubusercontent.com/Fmacedo87/iptv/master/Deportes.m3u",
    "https://raw.githubusercontent.com/m3u8playlist/free-iptv-channels/main/sport.m3u",
    "https://raw.githubusercontent.com/DeXTeR085/IPTV/main/Global.m3u"
]

def capturar_por_nombre(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=headers, timeout=25)
        # Captura el nombre del canal y el link
        matches = re.findall(r'#EXTINF:.*?,(.*?)\n(http.*?m3u8[^\s]*)', r.text)
        
        resultados = []
        for nombre, link in matches:
            nombre_up = nombre.upper()
            # Si el nombre del canal está en nuestra lista de fútbol, lo guardamos
            if any(objetivo.upper() in nombre_up for objetivo in NOMBRES_FUTBOL):
                # Filtro básico: fuera radio y adultos
                if not any(b in nombre_up for b in ["RADIO", "XXX", "ADULT"]):
                    resultados.append(f"{nombre.strip()}|{link.strip()}")
        return resultados
    except:
        return []

def asalto_nombres_total():
    print("📡 Iniciando barrido masivo por nombres de canales...")
    botin_nombres = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        listas = list(executor.map(capturar_por_nombre, FUENTES_MUNDIALES))
    
    for l in listas:
        botin_nombres.extend(l)

    # Eliminar duplicados para que la lista sea limpia
    botin_final = sorted(list(set(botin_nombres)))

    with open("lista_canales.txt", "w", encoding='utf-8') as f:
        if botin_final:
            f.write("\n".join(botin_final))
            print(f"🏁 ¡MISIÓN CUMPLIDA! Se capturaron {len(botin_final)} canales de fútbol por nombre.")
        else:
            f.write("ERROR|No se encontraron canales con los nombres solicitados.")

if __name__ == "__main__":
    asalto_nombres_total()
    
