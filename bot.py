import requests
from bs4 import BeautifulSoup
import os

# DISFRAZ DE ÉLITE (iPhone + Referer)
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/605.1',
    'Referer': 'https://www.google.com/'
}

def mision_alfa_web1():
    print("[*] Escaneando Web 1 (MadPlay)...")
    url = "https://ganzqowo.ps34buy87z6lothrough.sbs/es/"
    lista = []
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            if any(x in link['href'] for x in ['/football/', '/basketball/']):
                nombre = link.text.strip().upper()
                if len(nombre) > 5: lista.append(f"W1: {nombre}|{link['href']}")
    except: pass
    return lista

def mision_bravo_web2():
    print("[*] Verificando Web 2 (24/7)...")
    url = "https://stream2watch.pk/s2w/808"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if "vveetchit.my/embed/stream-73.php" in r.text:
            return "W2: STREAM2WATCH VIP|https://vveetchit.my/embed/stream-73.php"
    except: return None

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
    url = "https://vipleague.io/football-schedule-streaming-links"
    lista = []
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(r.text, 'html.parser')
        # Buscamos eventos que tengan ' VS ' para asegurar que son partidos
        for link in soup.find_all('a', href=True):
            texto = " ".join(link.get_text(separator=" ").split()).upper()
            if " VS " in texto and "/football/" in link['href']:
                full_link = link['href'] if link['href'].startswith('http') else f"https://vipleague.io{link['href']}"
                lista.append(f"VIP: {texto}|{full_link}")
    except: pass
    return lista

def ejecutar_operacion():
    total = mision_alfa_web1()
    c247 = mision_bravo_web2()
    if c247: total.append(c247)
    total.extend(mision_charlie_web3())
    total.extend(mision_echo_vipleague())

    # Eliminar duplicados y basura
    total = list(set(total))

    with open("lista_canales.txt", "w") as f:
        f.write("\n".join(total))

    print(f"\n[!] VICTORIA: {len(total)} canales capturados.")
    os.system("git add . && git commit -m 'Restauración y limpieza multifuente' && git push origin main")

if __name__ == "__main__":
    ejecutar_operacion()
