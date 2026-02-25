import requests
import re
import base64

# Tus objetivos estratégicos
URLS = [
    "https://teledeportes.top/stream-tv.php",
    "https://antenasport.top",
    "https://daddyhd.com",
    "https://dlhd.link"
]

def decodificar_base64(texto):
    try:
        # Algunos sitios esconden el .m3u8 en base64
        return base64.b64decode(texto).decode('utf-8')
    except:
        return None

def asalto_final(url):
    # Disfraz de navegador móvil (más difícil de bloquear)
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
        'Referer': url,
        'Accept': '*/*'
    }
    try:
        r = requests.get(url, headers=headers, timeout=15)
        html = r.text

        # 1. Buscar link directo
        directo = re.findall(r'(https?://[^\s\'"]+\.m3u8[^\s\'"]*)', html)
        if directo:
            return directo[0].replace('\\/', '/')

        # 2. Buscar links escondidos en variables 'source' o 'file'
        escondido = re.search(r'(?:file|source|src):\s*["\']([^"\']+\.m3u8[^"\']*)["\']', html)
        if escondido:
            return escondido.group(1).replace('\\/', '/')

    except:
        pass
    return None

def iniciar_mision():
    print("📡 Iniciando barrido de frecuencias...")
    botin = []
    
    for i, url in enumerate(URLS):
        link = asalto_final(url)
        if link:
            print(f"✅ OBJETIVO CAPTURADO: {url}")
            botin.append(f"CANAL_{i+1}|{link}")
        else:
            print(f"❌ Escudo impenetrable en: {url}")

    # Forzamos la creación del archivo para que GitHub no de error
    with open("lista_canales.txt", "w") as f:
        if botin:
            f.write("\n".join(botin))
        else:
            f.write("ERROR|Los 226 sitios tienen las defensas altas. Reintentando...")
    
    print("🏁 Misión finalizada.")

if __name__ == "__main__":
    iniciar_mision()
    
