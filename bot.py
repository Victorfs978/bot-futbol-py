import requests
import re
from concurrent.futures import ThreadPoolExecutor

# --- ELITE DE FUENTES (Menos cantidad, más calidad) ---
FUENTES_PREMIUM = [
    "https://raw.githubusercontent.com/DeXTeR085/IPTV/main/Global.m3u",
    "https://raw.githubusercontent.com/Lundis/IPTV-World/master/IPTV.m3u",
    "https://raw.githubusercontent.com/Soky9/TV/main/Sport.m3u"
]

# --- RADAR DE FÚTBOL PREMIUM ---
NOMBRES_ORO = [
    "ESPN PREMIUM", "FOX SPORTS PREMIUM", "TYC SPORTS HD", "TIGO SPORTS HD",
    "WIN SPORTS+", "DIRECTV SPORTS HD", "DSPORTS HD", "TNT SPORTS HD",
    "DAZN F1", "BEIN SPORTS 1 HD", "MOVISTAR LALIGA", "SKY SPORTS MAIN EVENT",
    "PREMIER LEAGUE TV", "CANAL+ SPORT HD", "GOL PLAY HD", "TUDN HD"
]

def inspeccion_de_elite(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    try:
        r = requests.get(url, headers=headers, timeout=20)
        # Buscamos el patrón: Nombre y URL
        matches = re.findall(r'#EXTINF:.*?,(.*?)\n(http.*?m3u8[^\s]*)', r.text)
        
        filtrados = []
        for nombre, link in matches:
            n = nombre.upper()
            # 1. ¿Es de nuestra lista de ORO?
            if any(target in n for target in NOMBRES_ORO):
                # 2. FILTRO DE CALIDAD: Solo HD o 1080p, nada de mierda 360p
                if any(q in n for q in ["HD", "1080P", "4K", "FHD"]) or "premium" in n.lower():
                    # 3. FILTRO ANTI-BLOQUEO: Ignoramos links de servidores conocidos por fallar
                    if not any(b in link for b in ["iptv-org", "geo-blocked", "localhost"]):
                        filtrados.append(f"{nombre.strip()}|{link.strip()}")
        return filtrados
    except:
        return []

def ataque_calidad_total():
    print("🚀 Iniciando purga... buscando solo FÚTBOL HD PREMIUM.")
    botin_hd = []

    with ThreadPoolExecutor(max_workers=5) as executor:
        listas = list(executor.map(inspeccion_de_elite, FUENTES_PREMIUM))
    
    for l in listas:
        botin_hd.extend(l)

    # Eliminar repetidos
    botin_final = list(set(botin_hd))

    with open("lista_canales.txt", "w", encoding='utf-8') as f:
        if botin_final:
            f.write("\n".join(botin_final))
            print(f"✅ ¡MISIÓN CUMPLIDA! Se encontraron {len(botin_final)} canales de CALIDAD.")
        else:
            f.write("ERROR|La purga fue demasiado fuerte. No hay señales HD hoy.")

if __name__ == "__main__":
    ataque_calidad_total()
    
