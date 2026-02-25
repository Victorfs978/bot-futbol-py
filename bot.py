import requests
import re

# CONFIGURACIÓN DE SU IMPERIO
NEOCITIES_API_KEY = "da77c3530c30593663bf7b797323e48c"
USUARIO_NEOCITIES = "victorfs"

def enviar_botin_a_casa():
    print("📡 CAZANDO LOS 1500 LINKS DE FÚTBOL...")
    fuentes = [
        "https://iptv-org.github.io/iptv/languages/spa.m3u",
        "https://raw.githubusercontent.com/Guydun/Tv-online/main/Tv-online.m3u",
        "https://raw.githubusercontent.com/TheRealSanjeev/IPTV/main/Global/Sports.m3u"
    ]
    
    todos_los_links = []
    for url in fuentes:
        try:
            r = requests.get(url, timeout=15)
            enlaces = re.findall(r'(https?://[^\s"\'<>]+m3u8)', r.text)
            for l in enlaces:
                if l not in todos_los_links:
                    todos_los_links.append(l)
        except:
            continue

    # 1. Creamos la lista en un formato que Neocities acepte
    nombre_archivo = "lista_canales.txt"
    with open(nombre_archivo, "w") as f:
        f.write(f"--- LISTA DE {len(todos_los_links)} CANALES CAPTURADOS ---\n\n")
        for i, link in enumerate(todos_los_links):
            f.write(f"CANAL {i+1}: {link}\n")
    
    print(f"✅ {len(todos_los_links)} links listos. Enviando a https://{USUARIO_NEOCITIES}.neocities.org...")

    # 2. SUBIR A NEOCITIES
    try:
        url_api = "https://neocities.org/api/upload"
        headers = {"Authorization": f"Bearer {NEOCITIES_API_KEY}"}
        
        with open(nombre_archivo, "rb") as f:
            files = {nombre_archivo: f}
            response = requests.post(url_api, headers=headers, files=files)
            
        if response.status_code == 200:
            print(f"🚀 ¡MISIÓN CUMPLIDA! Mira tus links aquí:")
            print(f"👉 https://{USUARIO_NEOCITIES}.neocities.org/{nombre_archivo}")
        else:
            print(f"❌ Error al subir: {response.text}")
    except Exception as e:
        print(f"❌ Error fatal: {e}")

if __name__ == "__main__":
    enviar_botin_a_casa()
    
