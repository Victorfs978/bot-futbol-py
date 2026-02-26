import requests
from bs4 import BeautifulSoup
import os

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/605.1',
    'Referer': 'https://www.google.com/'
}

def mision_ataque_nuevo_servidor():
    url_base = "https://mayhypy.smnjdigv2pxjchest.cfd/es/"
    print(f"[*] Escaneando eventos en: {url_base}")
    lista = []
    try:
        r = requests.get(url_base, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            nombre = link.text.strip().upper()
            href = link['href']
            
            # FILTRO FRANCOTIRADOR: Solo si contiene "VS", " AT " o es un nombre largo de equipo
            # Y descartamos palabras de menú que detectamos en tu captura
            if len(nombre) > 12 and any(x in nombre for x in [" VS ", " AT ", "CLUB", "COPA", "GUARA"]):
                if not any(b in nombre for b in ["YOUTUBE", "POLÍTICA", "TÉRMINOS", "APK"]):
                    full_link = href if href.startswith('http') else f"https://mayhypy.smnjdigv2pxjchest.cfd{href}"
                    lista.append(f"PARTIDO: {nombre}|{full_link}")
                    print(f"[+] ¡EVENTO CONFIRMADO!: {nombre}")
    except: pass
    return lista

def mision_extra_vipleague():
    print("[*] Buscando refuerzos en VipLeague...")
    url = "https://vipleague.io/football-schedule-streaming-links"
    lista = []
    try:
        r = requests.get(url, headers=HEADERS, timeout=12)
        soup = BeautifulSoup(r.text, 'html.parser')
        for row in soup.find_all('div', class_='match-row'):
            link = row.find('a', href=True)
            if link:
                nombre = link.text.strip().upper()
                if " VS " in nombre or len(nombre) > 15:
                    lista.append(f"VIP-EVENTO: {nombre}|{link['href']}")
    except: pass
    return lista

def ejecutar_operacion():
    eventos = mision_ataque_nuevo_servidor() + mision_extra_vipleague()
    
    if not eventos:
        print("[!] No se encontraron partidos activos con 'VS'.")
    
    with open("lista_canales.txt", "w") as f:
        f.write("\n".join(eventos))
        
    print(f"\n[!] VICTORIA: {len(eventos)} eventos reales capturados.")
    os.system("git add . && git commit -m 'Filtro Francotirador: Solo partidos reales' && git push origin main")

if __name__ == "__main__":
    ejecutar_operacion()
