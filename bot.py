import requests
from bs4 import BeautifulSoup
import os

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/605.1',
    'Referer': 'https://www.google.com/'
}

# Lista de palabras que NO son partidos
BASURA = ["APK", "FÚTBOL", "BALONCESTO", "CRICKET", "HOCKEY", "BÁDMINTON", "VOLEIBOL", "CICLISMO", "BALONMANO", "BÉISBOL", "TELEGRAM", "POLÍTICA", "TÉRMINOS", "YOUTUBE", "FORMULA 1", "EN VIVO", "FUTBOL AMERICANO", "FÚTBOL AUS"]

def mision_ataque_nuevo_servidor():
    url_base = "https://mayhypy.smnjdigv2pxjchest.cfd/es/"
    print(f"[*] Atacando servidor: {url_base}")
    lista = []
    try:
        r = requests.get(url_base, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            nombre = link.text.strip().upper()
            href = link['href']
            
            # FILTRO INTELIGENTE: Si el nombre es largo y NO está en la lista negra
            if len(nombre) > 10 and not any(b in nombre for b in BASURA):
                full_link = href if href.startswith('http') else f"https://mayhypy.smnjdigv2pxjchest.cfd{href}"
                lista.append(f"LIBERTADORES: {nombre}|{full_link}")
                print(f"[+] PARTIDO CAPTURADO: {nombre}")
    except: pass
    return lista

def mision_extra_vipleague():
    print("[*] Reforzando con VipLeague...")
    url = "https://vipleague.io/football-schedule-streaming-links"
    lista = []
    try:
        r = requests.get(url, headers=HEADERS, timeout=12)
        soup = BeautifulSoup(r.text, 'html.parser')
        for row in soup.find_all('div', class_='match-row'):
            link = row.find('a', href=True)
            if link:
                nombre = link.text.strip().upper()
                if len(nombre) > 5:
                    lista.append(f"VIP-LEAGUE: {nombre}|{link['href']}")
    except: pass
    return lista

def ejecutar_operacion():
    eventos = mision_ataque_nuevo_servidor() + mision_extra_vipleague()
    with open("lista_canales.txt", "w") as f:
        f.write("\n".join(eventos))
    print(f"\n[!] VICTORIA: {len(eventos)} partidos reales capturados.")
    os.system("git add . && git commit -m 'Filtro de eventos activado' && git push origin main")

if __name__ == "__main__":
    ejecutar_operacion()
