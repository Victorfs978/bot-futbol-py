import requests, re, os
from bs4 import BeautifulSoup

HEADERS = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)'}

def mision_alfa_web1():
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

def mision_fox_tp10():
    print("[*] Perforando Búnker StreamTP10...")
    url = "https://streamtp10.com/"
    lista = []
    h = {'User-Agent': 'Mozilla/5.0', 'Referer': url}
    try:
        r = requests.get(url, headers=h, timeout=10)
        canales = re.findall(r'global1\.php\?stream=([^"]+)', r.text)
        for c in set(canales):
            try:
                r2 = requests.get(f"{url}global1.php?stream={c}", headers=h, timeout=5)
                iframe = re.search(r'iframe.*?src=["\']([^"\']+)["\']', r2.text)
                if iframe: lista.append(f"TP10: {c.upper()}|{iframe.group(1)}")
            except: continue
    except: pass
    return lista

def ejecutar():
    total = mision_alfa_web1()
    total.extend(mision_fox_tp10())
    # ... (simplificado para que entre el búnker)
    with open("lista_canales.txt", "w") as f:
        f.write("\n".join(total))
    print(f"[!] VICTORIA: {len(total)} canales capturados.")
    os.system('git add . && git commit -m "Infiltracion TP10 Exitosa" && git push origin main')

if __name__ == "__main__":
    ejecutar()
