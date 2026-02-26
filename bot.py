import requests
from bs4 import BeautifulSoup
import os

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/605.1',
    'Referer': 'https://www.google.com/'
}

def mision_ataque_nuevo_servidor():
    # URL del nuevo servidor que detectaste
    url_base = "https://mayhypy.smnjdigv2pxjchest.cfd/es/"
    print(f"[*] Atacando servidor: {url_base}")
    lista = []
    try:
        r = requests.get(url_base, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        # Buscamos todos los enlaces de la página
        for link in soup.find_all('a', href=True):
            nombre = link.text.strip().upper()
            href = link['href']
            
            # Filtro de Fuerza Bruta: Si tiene nombre y no es un link interno genérico
            if nombre and len(nombre) > 5 and not any(x in nombre for x in ["INICIO", "CONTACTO", "POLITICA"]):
                # Si el link es relativo, le pegamos la base
                full_link = href if href.startswith('http') else f"https://mayhypy.smnjdigv2pxjchest.cfd{href}"
                lista.append(f"EVENTO: {nombre}|{full_link}")
                print(f"[+] Capturado: {nombre[:40]}...")
    except Exception as e:
        print(f"[!] Error en el asalto: {e}")
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
                lista.append(f"VIP-LEAGUE: {nombre}|{link['href']}")
    except: pass
    return lista

def ejecutar_operacion():
    print("🔥 INICIANDO RECOLECCIÓN DE EVENTOS...")
    
    # Prioridad absoluta al nuevo servidor
    eventos_principales = mision_ataque_nuevo_servidor()
    eventos_secundarios = mision_extra_vipleague()
    
    todo = eventos_principales + eventos_secundarios

    with open("lista_canales.txt", "w") as f:
        f.write("\n".join(todo))

    print(f"\n[!] VICTORIA: {len(todo)} eventos capturados del nuevo dominio.")
    os.system("git add . && git commit -m 'Asalto masivo al nuevo servidor' && git push origin main")
    print("[+] Botín enviado a GitHub.")

if __name__ == "__main__":
    ejecutar_operacion()
