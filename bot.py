import requests
import re

# Probemos con estos objetivos que son los más estables de tu lista
URLS = [
    "https://teledeportes.top/stream-tv.php",
    "https://antenasport.top",
    "https://strumyk.uk",
    "https://daddyhd.com"
]

def capturador_pro(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36',
        'Referer': 'https://google.com'
    }
    try:
        # Usamos un tiempo de espera más largo por si la web es lenta
        r = requests.get(url, headers=headers, timeout=20)
        # Buscamos m3u8 incluso si está oculto en el código fuente
        links = re.findall(r'(https?://[^\s\'"]+\.m3u8[^\s\'"]*)', r.text)
        if links:
            return links[0].replace('\\/', '/')
    except:
        return None
    return None

def iniciar():
    print("🕵️ Buscando transmisiones...")
    final = []
    for i, url in enumerate(URLS):
        link = capturador_pro(url)
        if link:
            print(f"✅ ¡GOL! Capturado en: {url}")
            final.append(f"CANAL_{i+1}|{link}")
        else:
            print(f"❌ Fallo en: {url}")
    
    # IMPORTANTE: Creamos el archivo aunque esté vacío para que GitHub no se queje
    with open("lista_canales.txt", "w") as f:
        if final:
            f.write("\n".join(final))
        else:
            f.write("MANTENIMIENTO|Buscando señales nuevas...")
    print("📂 Proceso terminado.")

if __name__ == "__main__":
    iniciar()
    
