import requests
import re
import base64
from concurrent.futures import ThreadPoolExecutor

# AQUÍ VA TU LISTA COMPLETA DE 226 URLS (He puesto las principales, pega todas las que tengas)
OBJETIVOS = [
    "https://www.camel1.live", "https://antenasport.top", "https://strumyk.uk",
    "https://daddyhd.com", "https://dlhd.link", "https://teledeportes.top/stream-tv.php",
    "https://tudeporte.pro", "https://nowevents.xyz", "https://sosplay.net",
    "https://deporte-libre.click/", "https://pelotalibretv.su", "https://la14hd.com"
    # ... pega el resto de tus 226 aquí
]

def desarmar_sitio(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
        'Referer': url
    }
    try:
        r = requests.get(url, headers=headers, timeout=10)
        html = r.text
        
        # 1. Buscar M3U8 Directo
        m3u = re.search(r'["\'](https?://[^\s\'"]+\.m3u8[^\s\'"]*)["\']', html)
        if m3u: return m3u.group(1).replace('\\/', '/')
        
        # 2. Buscar Iframe del reproductor
        ifr = re.search(r'<iframe.*?src=["\']([^"\']+)["\']', html)
        if ifr:
            link = ifr.group(1)
            if link.startswith('//'): link = "https:" + link
            return link
            
        # 3. Buscar Base64 (Trabajo sucio)
        b64 = re.findall(r'["\']([A-Za-z0-9+/]{40,})={0,2}["\']', html)
        for b in b64:
            try:
                dec = base64.b64decode(b).decode('utf-8')
                if ".m3u8" in dec: return dec
            except: continue
    except:
        return None
    return None

def ejecutar_ataque():
    print(f"🔥 LANZANDO ATAQUE TOTAL SOBRE {len(OBJETIVOS)} SITIOS...")
    botin = []
    
    # Atacamos con 10 hilos a la vez para no perder tiempo
    with ThreadPoolExecutor(max_workers=10) as executor:
        resultados = list(executor.map(desarmar_sitio, OBJETIVOS))
    
    for i, link in enumerate(resultados):
        if link:
            botin.append(f"CANAL_{i+1}|{link}")
            print(f"✅ CAPTURADO: {OBJETIVOS[i][:30]}...")

    with open("lista_canales.txt", "w", encoding='utf-8') as f:
        if botin:
            f.write("\n".join(botin))
        else:
            f.write("FALLO_TOTAL|Los 226 escudos resistieron. Necesitamos Proxys.")
    
    print(f"🏁 ASALTO TERMINADO. Presas: {len(botin)}")

if __name__ == "__main__":
    ejecutar_ataque()
    
