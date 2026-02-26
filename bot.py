import requests
from bs4 import BeautifulSoup
import os

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/605.1',
    'Referer': 'https://www.google.com/'
}

def mision_alfa_madplay():
    print("[*] Escaneando MadPlay (Fuerza Bruta)...")
    url = "https://ganzqowo.ps34buy87z6lothrough.sbs/es/"
    lista = []
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            nombre = link.text.strip().upper()
            href = link['href']
            # Capturamos todo lo que tenga nombre real para no perder eventos
            if nombre and len(nombre) > 3 and "HTTP" in href.upper():
                lista.append(f"MADPLAY: {nombre}|{href}")
    except: pass
    return lista

def mision_bravo_web2():
    print("[*] Verificando Stream2Watch VIP...")
    url = "https://stream2watch.pk/s2w/808"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if "vveetchit.my/embed/stream-73.php" in r.text:
            return "S2W: STREAM2WATCH VIP|https://vveetchit.my/embed/stream-73.php"
    except: return None

def mision_echo_vipleague():
    print("[*] Infiltrando VipLeague (Agendas)...")
    url = "https://vipleague.io/football-schedule-streaming-links"
    lista = []
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(r.text, 'html.parser')
        for row in soup.find_all('div', class_='match-row'):
            link = row.find('a', href=True)
            if link:
                nombre = link.text.strip().upper()
                if nombre: lista.append(f"VIP-LEAGUE: {nombre}|{link['href']}")
    except: pass
    return lista

def ejecutar_operacion():
    total = mision_alfa_madplay()
    
    c247 = mision_bravo_web2()
    if c247: total.append(c247)
    
    total.extend(mision_echo_vipleague())

    with open("lista_canales.txt", "w") as f:
        f.write("\n".join(total))

    print(f"\n[!] OPERACIÓN LIMPIA: {len(total)} eventos de calidad capturados.")
    os.system("git add . && git commit -m 'Limpieza: AntenaSport eliminado' && git push origin main")
    print("[+] GitHub actualizado sin basura.")

if __name__ == "__main__":
    ejecutar_operacion()
