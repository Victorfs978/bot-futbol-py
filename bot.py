import requests
from bs4 import BeautifulSoup
import os
import re

# Configuración de Identidad (Disfraz)
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)'}

def mision_alfa_web1():
    print("[*] Escaneando Web 1 (MadPlay)...")
    url = "https://ganzomo.ps4buy8z6btothrough.sbs/es/"
    lista = []
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            if any(x in link['href'] for x in ['/football/', '/basketball/']):
                nombre = link.text.strip().upper()
                if nombre: lista.append(f"M1: {nombre}|{link['href']}")
    except: pass
    return lista

def mision_bravo_web2():
    print("[*] Verificando Web 2 (24/7)...")
    url = "https://stream2watch.pk/s2w/008"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if 'vveetchit.my/embed/stream-73.php' in r.text:
            return ["W2: STREAM2WATCH VIP|https://vveetchit.my/embed/stream-73.php"]
    except: pass
    return []

def mision_charlie_web3():
    print("[*] Escaneando Web 3 (AntenaSport)...")
    url = "https://antenasport.top/"
    lista = []
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        for a in soup.find_all('a', href=True):
            if 'antenasport.top/' in a['href'] and '.php' in a['href']:
                nombre = a.text.strip().upper()
                if nombre and "INICIO" not in nombre:
                    lista.append(f"W3: CANAL {len(lista)+1} VIP|{a['href']}")
    except: pass
    return lista

def mision_echo_vipleague():
    print("[*] Infiltrando Nueva Víctima (VipLeague)...")
    url = "https://vipleague.im/football-schedule-streaming-links"
    lista = []
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(r.text, 'html.parser')
        for row in soup.find_all('div', class_='match-row'):
            link = row.find('a', href=True)
            if link:
                nombre = link.text.strip().upper()
                if nombre: lista.append(f"FVIP: {nombre}|{link['href']}")
    except: pass
    return lista

def mision_fox_tp10():
    print("[*] Infiltrando Búnker (StreamTP10)...")
    url = "https://streamtp10.com/"
    lista = []
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        canales = re.findall(r'global1\.php\?stream=([^"]+)', r.text)
        for c in set(canales):
            try:
                target = f"{url}global1.php?stream={c}"
                r2 = requests.get(target, headers={'User-Agent': HEADERS['User-Agent'], 'Referer': url}, timeout=5)
                iframe = re.search(r'iframe.*?src="([^"]+)"', r2.text)
                if iframe:
                    lista.append(f"TP10: {c.upper()}|{iframe.group(1)}")
            except: continue
    except: pass
    return lista

def ejecutar_operacion():
    total = []
    total.extend(mision_alfa_web1())
    
    c247 = mision_bravo_web2()
    if c247: total.extend(c247)
    
    total.extend(mision_charlie_web3())
    total.extend(mision_echo_vipleague())
    
    # AQUÍ AGREGAMOS LA QUINTA FUENTE
    total.extend(mision_fox_tp10())

    with open("lista_canales.txt", "w") as f:
        f.write("\n".join(total))

    print(f"[!] VICTORIA: {len(total)} canales de 5 fuentes capturados.")
    os.system('git add . && git commit -m "Actualización Masiva: 5 Fuentes VIP (Infiltración TP10)" && git push origin main')
    print("[+] GitHub actualizado.")

if __name__ == "__main__":
    ejecutar_operacion()

