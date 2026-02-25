import requests
import re

# OBJETIVOS MADRE (Sitios que centralizan múltiples ligas)
SITIOS_MADRE = [
    "https://teledeportes.top/stream-tv.php",
    "https://antenasport.top",
    "https://deporte-libre.click/",
    "https://tudeporte.pro"
]

def extraer_iframe_limpio(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36',
        'Referer': 'https://google.com'
    }
    try:
        r = requests.get(url, headers=headers, timeout=15)
        # Buscamos el src de los iframes que contienen el reproductor
        iframes = re.findall(r'<iframe.*?src=["\'](.*?)["\']', r.text)
        
        for link in iframes:
            # Filtramos basura (anuncios y trackers comunes)
            if any(x in link for x in ["facebook", "twitter", "google", "ads", "analytics"]):
                continue
            
            # Normalizamos el link para que sea una URL completa
            if link.startswith('//'):
                link = "https:" + link
            elif not link.startswith('http'):
                link = url + link
                
            return link # Retorna la primera puerta válida encontrada
    except:
        return None
    return None

def mision_asalto_hibrido():
    print("📡 Iniciando rastreo de puertas (Iframes)...")
    resultados = []
    
    for i, url in enumerate(SITIOS_MADRE):
        iframe_url = extraer_iframe_limpio(url)
        if iframe_url:
            print(f"✅ PUERTA ABIERTA EN: {url}")
            # Formato listo para su lista_canales.txt en Sketchware
            resultados.append(f"CANAL_FUTBOL_{i+1}|{iframe_url}")
        else:
            print(f"❌ Muralla detectada en: {url}")

    # Escribimos el botín en el archivo que ya conoce su Main
    with open("lista_canales.txt", "w", encoding='utf-8') as f:
        if resultados:
            f.write("\n".join(resultados))
        else:
            f.write("ESTADO|Buscando señales... Reintente en 5 min.")
            
    print(f"🏁 Misión terminada. Se encontraron {len(resultados)} puertas.")

if __name__ == "__main__":
    mision_asalto_hibrido()
    
