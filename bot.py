import requests
import re
import os

def guardar_y_forzar_subida():
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
            enlaces = re.findall(r'(https?://[^\s"\'<>]+m3u8)', r.text)
            for l in enlaces:
                if l not in todos_los_links:
                    todos_los_links.append(l)
        except:
            continue

    # Creamos el archivo
    with open("lista_canales.txt", "w") as f:
        for i, link in enumerate(todos_los_links):
            f.write(f"CANAL {i+1}: {link}\n")
    
    print(f"✅ {len(todos_los_links)} links listos. Forzando subida a Code...")

    # COMANDOS DE FUERZA BRUTA PARA QUE APAREZCA
    os.system('git config --local user.name "Victorfs978"')
    os.system('git config --local user.email "victorfs978@github.com"')
    os.system('git add lista_canales.txt')
    os.system('git commit -m "Lista de 1500 links lista"')
    # Usamos el token automático de GitHub para el push
    os.system('git push https://x-access-token:${{ github.token }}@github.com/${{ github.repository }} HEAD:main')

if __name__ == "__main__":
    guardar_y_forzar_subida()
    
