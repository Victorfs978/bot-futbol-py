import requests, re, os, time
from bs4 import BeautifulSoup

# Identidad de infiltración
H = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def mision_castmedia():
    print("[*] Atacando CastMedia: Extrayendo agenda de eventos...")
    url = "https://castmedia.click/"
    lista = []
    try:
        r = requests.get(url, headers=H, timeout=15)
        # Extraemos todos los enlaces .php (como los de flixxlive.pro que viste)
        enlaces = re.findall(r'https?://[^\s<>"]+\.php', r.text)
        
        for link in set(enlaces):
            # Limpiamos el nombre para que quede bien en tu app
            nombre_sucio = link.split('/')[-1].replace('.php', '').replace('_', ' ').upper()
            lista.append(f"CAST: {nombre_sucio}|{link}")
            print(f"[+] Capturado: {nombre_sucio}")
    except Exception as e: 
        print(f"[-] Error en el asalto: {e}")
    return lista

def ejecutar_operacion():
    print("[*] Iniciando ciclo de sangrado...")
    botin = mision_castmedia()
    
    # Escribimos los resultados en el archivo
    with open("lista_canales.txt", "w") as f:
        f.write("\n".join(botin))
    
    print(f"[!] VICTORIA: {len(botin)} canales extraídos de CastMedia.")
    
    # Subida automática a tu búnker de GitHub
    if len(botin) > 0:
        os.system('git add . && git commit -m "Asalto Exitoso: CastMedia Infiltrado" && git push origin main')
        print("[+] Botín asegurado en GitHub.")

if __name__ == "__main__":
    ejecutar_operacion()
