import requests
import re
import base64
from concurrent.futures import ThreadPoolExecutor

# LISTA MAESTRA DE 226 URLS (Añade todas las que faltan aquí)
OBJETIVOS = [
    "https://www.camel1.live", "https://antenasport.top", "https://strumyk.uk",
    "https://daddyhd.com", "https://dlhd.link", "https://teledeportes.top/stream-tv.php",
    "https://tudeporte.pro", "https://nowevents.xyz", "https://sosplay.net",
    "https://deporte-libre.click/", "https://pelotalibretv.su", "https://la14hd.com",
    "https://streameast100.is", "https://totalsportek.army", "https://www.footybite.to"
]

def desarmar_sitio(url):
    # Disfraz de iPhone para saltar bloqueos básicos
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
        'Referer': url
    }
    try:
        r = requests.get(url, headers=headers, timeout=12)
        html = r.text
        
        # 1. Búsqueda de M3U8 Directo (con o sin tokens)
        m3u = re.search(r'["\'](https?://[^\s\'"]+\.m3u8[^\s\'"]*)["\']', html)
        if m3u: return m3u.group(1).replace('\\/', '/')
        
        # 2. Captura de Iframe (La puerta trasera estable)
        ifr = re.search(r'<iframe.*?src=["\']([^"\']+)["\']', html)
        if ifr:
            link = ifr.group(1)
            if link.startswith('//'): link = "https:" + link
            return link
            
        # 3. Trabajo Sucio: Decodificar Base64 oculto
        b64_matches = re.findall(r'["\']([A-Za-z0-9+/]{40,})={0,2}["\']', html)
        for b in b64_matches:
            try:
                dec = base64.b64decode(b).decode('utf-8')
                if ".m3u8" in dec: return dec
            except: continue
    except:
        return None
    return None

def ejecutar_ataque_total():
    print(f"🔥 LANZANDO OFENSIVA SOBRE {len(OBJETIVOS)} OBJETIVOS...")
    botin = []
    
    # Atacamos con 15 hilos en paralelo para máxima velocidad
    with ThreadPoolExecutor(max_workers=15) as executor:
        resultados = list(executor.map(desarmar_sitio, OBJETIVOS))
    
    for i, link in enumerate(resultados):
        if link:
            # Formato optimizado para tu App en Sketchware
            botin.append(f"CANAL_{i+1}|{link}")
            print(f"✅ CAPTURADO: {OBJETIVOS[i]}")

    # Guardar el botín en el Centro de Mando
    with open("lista_canales.txt", "w", encoding='utf-8') as f:
        if botin:
            f.write("\n".join(botin))
        else:
            f.write("ERROR|Defensas enemigas demasiado altas. Se requiere refuerzo de Proxys.")
    
    print(f"🏁 ASALTO FINALIZADO. Presas conseguidas: {len(botin)}")

if __name__ == "__main__":
    ejecutar_ataque_total()
    
