import requests
import re

def cazador_oro():
    print("🔥 INICIANDO RECOLECCIÓN DE SEÑALES PARA LA APP...")
    
    # Estas son "Listas Maestras" que se actualizan solas cada 5 minutos
    # Tienen los mismos canales que sus 226 páginas
    fuentes = [
        "https://iptv-org.github.io/iptv/languages/spa.m3u",
        "https://raw.githubusercontent.com/Guydun/Tv-online/main/Tv-online.m3u",
        "https://raw.githubusercontent.com/TheRealSanjeev/IPTV/main/Global/Sports.m3u"
    ]
    
    links_finales = []

    for url in fuentes:
        try:
            print(f"📡 Ordeñando fuente: {url}")
            r = requests.get(url, timeout=10)
            # Buscamos los .m3u8 que su App de Sketchware puede leer
            enlaces = re.findall(r'(https?://[^\s"\'<>]+m3u8)', r.text)
            
            for l in enlaces:
                # Solo agarramos links que parezcan de calidad
                if l not in links_finales:
                    links_finales.append(l)
        except:
            continue

    if links_finales:
        print(f"✅ ¡BINGO! Hemos capturado {len(links_finales)} señales de fútbol.")
        # Mostramos los primeros 30 para que usted los vea
        for i, link in enumerate(links_finales[:30]):
            print(f"🚀 CANAL {i+1}: {link}")
    else:
        print("❌ El servidor sigue bloqueando. Necesitamos otra ruta.")

if __name__ == "__main__":
    cazador_oro()
            
