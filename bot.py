import requests
import re

# Sus objetivos estratégicos
URLS = [
    "https://teledeportes.top/stream-tv.php",
    "https://antenasport.top",
    "https://daddyhd.com",
    "https://dlhd.link"
]

def capturar_dinamico(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Referer': url
    }
    try:
        # 1. Primer intento: Buscar en la página principal
        r = requests.get(url, headers=headers, timeout=15)
        html = r.text
        
        # Buscamos el m3u8 directo
        match = re.search(r'["\'](https?://[^\s\'"]+\.m3u8[^\s\'"]*)["\']', html)
        if match:
            return match.group(1).replace('\\/', '/')

        # 2. Segundo intento: Buscar IFRAMES (La mayoría de los piratas esconden el video aquí)
        iframes = re.findall(r'<iframe.*?src=["\'](.*?)["\']', html)
        for frame_url in iframes:
            if not frame_url.startswith('http'):
                continue # Saltar publicidad
            
            # Entramos al Iframe a buscar el tesoro
            r_frame = requests.get(frame_url, headers={'Referer': url}, timeout=10)
            match_frame = re.search(r'["\'](https?://[^\s\'"]+\.m3u8[^\s\'"]*)["\']', r_frame.text)
            if match_frame:
                return match_frame.group(1).replace('\\/', '/')
                
    except:
        pass
    return None

def mision_asalto():
    print("🚀 Iniciando asalto a los servidores...")
    capturados = []
    
    for i, url in enumerate(URLS):
        link = capturar_dinamico(url)
        if link:
            print(f"✅ ¡PRESA CAZADA!: {url}")
            capturados.append(f"CANAL_{i+1}|{link}")
        else:
            print(f"❌ Sitio blindado: {url}")

    # Guardamos el botín
    with open("lista_canales.txt", "w") as f:
        if capturados:
            f.write("\n".join(capturados))
        else:
            # Si no captura nada, escribimos esto para saber que el bot falló en la búsqueda
            f.write("ERROR|Los sitios detectaron el bot. Necesitamos cambiar de estrategia.")

if __name__ == "__main__":
    mision_asalto()
    
