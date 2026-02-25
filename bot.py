import requests
import re

def guardar_todo_el_botin():
    print("📡 BUSCANDO LOS 1500 LINKS...")
    
    fuentes = [
        "https://iptv-org.github.io/iptv/languages/spa.m3u",
        "https://raw.githubusercontent.com/Guydun/Tv-online/main/Tv-online.m3u",
        "https://raw.githubusercontent.com/TheRealSanjeev/IPTV/main/Global/Sports.m3u"
    ]
    
    todos_los_links = []
    
    for url in fuentes:
        try:
            r = requests.get(url, timeout=15)
            # Buscamos cada link que termine en m3u8
            enlaces = re.findall(r'(https?://[^\s"\'<>]+m3u8)', r.text)
            for l in enlaces:
                if l not in todos_los_links:
                    todos_los_links.append(l)
        except:
            continue

    # AQUÍ ESTÁ EL TRUCO: Guardamos todo en un archivo .txt
    print(f"📝 Guardando {len(todos_los_links)} links en lista_canales.txt...")
    with open("lista_canales.txt", "w") as f:
        for i, link in enumerate(todos_los_links):
            f.write(f"CANAL {i+1}: {link}\n")
    
    print("✅ ¡ARCHIVO CREADO CON ÉXITO!")

if __name__ == "__main__":
    guardar_todo_el_botin()
    
            
