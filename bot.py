import requests
import re

# Objetivos de asalto
URLS = [
    "https://teledeportes.top/stream-tv.php",
    "https://antenasport.top",
    "https://deporte-libre.click/",
    "https://tudeporte.pro",
    "https://daddyhd.com",
    "https://dlhd.link"
]

def capturar_fuerza_bruta(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1',
        'Referer': 'https://google.com/',
        'Origin': url
    }
    try:
        # Petición con disfraz de iPhone
        r = requests.get(url, headers=headers, timeout=15)
        html = r.text

        # 1. Buscar .m3u8 (incluye links con tokens)
        m3u8 = re.search(r'["\'](https?://[^\s\'"]+\.m3u8[^\s\'"]*)["\']', html)
        if m3u8:
            return m3u8.group(1).replace('\\/', '/')

        # 2. Si no hay m3u8, capturar el IFRAME del reproductor
        iframe = re.search(r'<iframe.*?src=["\']([^"\']+)["\']', html)
        if iframe:
            link = iframe.group(1)
            if link.startswith('//'): link = "https:" + link
            return link

    except:
        return None
    return None

def ejecutar():
    print("📡 Iniciando captura...")
    botin = []
    for i, url in enumerate(URLS):
        link = capturar_fuerza_bruta(url)
        if link:
            botin.append(f"CANAL_{i+1}|{link}")
            print(f"✅ CAPTURADO: {url}")
        else:
            print(f"❌ FALLO: {url}")

    # Guardar resultados
    with open("lista_canales.txt", "w", encoding='utf-8') as f:
        if botin:
            f.write("\n".join(botin))
        else:
            f.write("ERROR|No se pudo romper la seguridad de ningún canal.")
    print("🏁 Fin del proceso.")

if __name__ == "__main__":
    ejecutar()
    
