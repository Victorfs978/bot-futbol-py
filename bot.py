import requests
import re

# Tus objetivos principales
URLS = [
    "https://www.camel1.live", "https://antenasport.top", "https://strumyk.uk",
    "https://daddyhd.com", "https://dlhd.link", "https://teledeportes.top/stream-tv.php"
    # ... (el resto de tus 226 URLs)
]

def caza_extrema(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Referer': url,
        'Accept-Language': 'es-ES,es;q=0.9'
    }
    try:
        # 1. Intentamos entrar al sitio
        r = requests.get(url, headers=headers, timeout=15)
        
        # 2. Buscamos cualquier rastro de m3u8 (incluso si está escapado como http:\/\/...)
        encontrado = re.findall(r'https?[:\\/]+[^\s\'"<>]+?\.m3u8[^\s\'"<>]*', r.text)
        
        if encontrado:
            # Limpiamos el link de posibles barras invertidas de JS
            link = encontrado[0].replace('\\/', '/')
            return link
    except:
        return None
    return None

def mision():
    final_list = []
    print(f"🚀 Comandante, iniciando asalto a {len(URLS)} sitios...")
    
    for i, u in enumerate(URLS):
        link = caza_extrema(u)
        if link:
            print(f"✅ ¡PRESA CAPTURADA!: {u}")
            final_list.append(f"CANAL_{i+1},{link}")
        else:
            print(f"❌ Sitio vacío o protegido: {u}")

    # Solo guardamos si realmente encontramos algo
    if final_list:
        with open("lista_canales.txt", "w") as f:
            f.write("\n".join(final_list))
        print(f"📂 Archivo generado con {len(final_list)} canales.")
    else:
        print("⚠️ ALERTA: No se capturó nada. Los 226 sitios tienen escudos activos.")

if __name__ == "__main__":
    mision()
    
