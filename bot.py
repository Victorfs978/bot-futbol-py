import requests
import re

# URLs de tu lista que suelen pasar Tigo Sports
URLS_TIGO = [
    "https://teledeportes.top/stream-tv.php",
    "https://antenasport.top",
    "https://deporte-libre.click/",
    "https://pelotalibretv.su"
]

def capturar_tigo(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Referer': url
    }
    try:
        # Entramos a la web que tiene el canal
        r = requests.get(url, headers=headers, timeout=15)
        
        # BUSQUEDA NIVEL 1: Link directo en el código
        directo = re.findall(r'(https?://[^\s\'"]+\.m3u8[^\s\'"]*)', r.text)
        if directo:
            return directo[0].replace('\\/', '/')

        # BUSQUEDA NIVEL 2: Buscamos el Iframe donde se oculta el reproductor
        iframe = re.search(r'<iframe.*?src=["\'](.*?)["\']', r.text)
        if iframe:
            url_frame = iframe.group(1)
            if not url_frame.startswith('http'):
                url_frame = "https:" + url_frame if url_frame.startswith('//') else url + url_frame
            
            # Entramos al Iframe
            r_frame = requests.get(url_frame, headers={'Referer': url}, timeout=10)
            # Buscamos el m3u8 dentro del script del reproductor
            m3u8_f = re.search(r'["\'](https?://[^\s\'"]+\.m3u8[^\s\'"]*)["\']', r_frame.text)
            if m3u8_f:
                return m3u8_f.group(1).replace('\\/', '/')
    except:
        return None
    return None

def ejecutar_mision():
    print("🛰️ Buscando la señal de Tigo Sports...")
    resultados = []
    
    for i, url in enumerate(URLS_TIGO):
        link = capturar_tigo(url)
        if link:
            print(f"✅ TIGO SPORTS CAPTURADO en: {url}")
            resultados.append(f"TIGO_SPORTS_{i+1}|{link}")
    
    # Escribimos el archivo para Sketchware
    with open("lista_canales.txt", "w") as f:
        if resultados:
            f.write("\n".join(resultados))
        else:
            f.write("TIGO_SPORTS|SIN_SEÑAL_ACTIVA")
            print("❌ No se encontró la señal. Los piratas cambiaron el cifrado.")

if __name__ == "__main__":
    ejecutar_mision()
    
