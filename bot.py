import requests
import re
import os

# Lista simplificada para probar (agrega las 226 después si funciona esta)
URLS = [
    "https://teledeportes.top/stream-tv.php",
    "https://antenasport.top",
    "https://strumyk.uk",
    "https://daddyhd.com"
]

def extraer_directo(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Referer': url
    }
    try:
        response = requests.get(url, headers=headers, timeout=15)
        text = response.text
        
        # BUSCADOR NINJA: Encuentra .m3u8 incluso con barras raras o protecciones simples
        # Busca patrones tipo http...m3u8
        enlaces = re.findall(r'https?%3A%2F%2F[\w\.\/%-]+\.m3u8|https?://[\w\.\/%-]+\.m3u8', text)
        
        if enlaces:
            link = enlaces[0].replace('%3A', ':').replace('%2F', '/')
            return link
            
        # Si no lo encuentra, busca dentro de variables JS comunes
        js_link = re.search(r'source:\s*"([^"]+\.m3u8)"', text)
        if js_link:
            return js_link.group(1)
            
    except Exception as e:
        print(f"Error en {url}: {e}")
    return None

def ejecutar():
    resultados = []
    print("🛰️ Iniciando escaneo de señales...")
    
    for i, url in enumerate(URLS):
        link = extraer_directo(url)
        if link:
            print(f"✅ ¡CAPTURADO!: {url}")
            resultados.append(f"CANAL_{i+1}|{link}")
        else:
            print(f"❌ Sin señal: {url}")
            
    # CRÍTICO: Si no encontró nada, creamos el archivo con un aviso 
    # para que GitHub Actions NO de error de 'file not found'
    if not resultados:
        resultados.append("STATUS|No se capturaron señales en este ciclo")

    with open("lista_canales.txt", "w", encoding='utf-8') as f:
        f.write("\n".join(resultados))
    
    print("📂 Misión terminada. Archivo generado.")

if __name__ == "__main__":
    ejecutar()
    
