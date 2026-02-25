import requests
import re
import os

def guardar_y_publicar_botin():
    print("📡 CAZANDO LOS 1500 LINKS...")
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

    # 1. Guardamos el archivo localmente
    with open("lista_canales.txt", "w") as f:
        for i, link in enumerate(todos_los_links):
            f.write(f"CANAL {i+1}: {link}\n")
    
    print(f"✅ {len(todos_los_links)} links guardados. Subiendo al repositorio...")

    # 2. COMANDOS PARA QUE APAREZCA EN SU LISTA DE ARCHIVOS
    os.system('git config --global user.name "GitHub Action"')
    os.system('git config --global user.email "action@github.com"')
    os.system('git add lista_canales.txt')
    os.system('git commit -m "Actualizar lista de canales"')
    os.system('git push')

if __name__ == "__main__":
    guardar_y_publicar_botin()
    
