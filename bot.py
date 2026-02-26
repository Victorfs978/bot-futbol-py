import requests
from bs4 import BeautifulSoup
import os

# CONFIGURACIÓN DE DISFRAZ (iPhone 17)
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'}

def mision_alfa_web1():
    print("[*] Escaneando eventos en Web 1...")
    url = "https://ganzqowo.ps34buy87z6lothrough.sbs/es/"
    lista = []
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            if any(x in link['href'] for x in ['/football/', '/basketball/', '/volleyball/']):
                nombre = link.text.strip().upper()
                if nombre:
                    lista.append(f"{nombre}|{link['href']}")
    except: pass
    return lista

def mision_bravo_web2():
    print("[*] Verificando Canal 24/7 (Stream2Watch)...")
    url = "https://stream2watch.pk/s2w/808"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if "vveetchit.my/embed/stream-73.php" in r.text:
            return "STREAM2WATCH - CANAL 808|https://vveetchit.my/embed/stream-73.php"
    except: return None

def mision_charlie_web3():
    print("[*] Escaneando eventos en AntenaSport (Víctima 3)...")
    url = "https://antenasport.top/"
    lista = []
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        for a in soup.find_all('a', href=True):
            if 'antenasport.top/' in a['href'] and '.php' in a['href']:
                nombre = a.text.strip().upper()
                if nombre and "INICIO" not in nombre:
                    lista.append(f"ANTENA: {nombre}|{a['href']}")
    except: pass
    return lista

def ejecutar_operacion():
    # Unir todo el botín
    total = mision_alfa_web1()
    
    c247 = mision_bravo_web2()
    if c247: total.append(c247)
    
    web3 = mision_charlie_web3()
    total.extend(web3)
    
    # Guardar en la carpeta del repositorio
    archivo = "lista_canales.txt"
    with open(archivo, "w") as f:
        f.write("\n".join(total))
    
    print(f"\n[!] VICTORIA: {len(total)} canales totales capturados.")
    
    # Sincronizar con GitHub
    os.system("git add .")
    os.system("git commit -m 'Infiltración Triple Exitosa'")
    os.system("git push origin main")
    print("[+] GitHub actualizado con las 3 víctimas.")

if __name__ == "__main__":
    ejecutar_operacion()
