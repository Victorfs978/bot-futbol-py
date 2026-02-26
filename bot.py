import requests, re, os

H = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def mision_agenda_vip():
    print("[*] Recuperando nombres de partidos de CastMedia...")
    lista = []
    try:
        r = requests.get("https://castmedia.click/", headers=H, timeout=12)
        # Buscamos los links que tienen nombre de partido
        enlaces = re.findall(r'https?://[^\s<>"]+\.php', r.text)
        for link in set(enlaces):
            # Convertimos el nombre del archivo en el nombre del partido
            nombre_sucio = link.split('/')[-1].replace('.php', '').replace('_', ' ')
            nombre_final = nombre_sucio.upper()
            lista.append(f"EVENTO: {nombre_final}|{link}")
    except: pass
    return lista

def mision_canales_fijos():
    print("[*] Asegurando señales 24/7 de AntenaSport...")
    lista = []
    try:
        r = requests.get("https://antenasport.top/", headers=H, timeout=12)
        canales = re.findall(r'href="(https?://antenasport\.top/[^"]+\.php)"', r.text)
        for i, link in enumerate(set(canales), 1):
            lista.append(f"24-7: SEÑAL {i} PREMIUM|{link}")
    except: pass
    return lista

def ejecucion_final():
    print("🔥 RECONSTRUYENDO BASE DE DATOS...")
    partidos = mision_agenda_vip()
    estables = mision_canales_fijos()
    
    total = partidos + estables
    
    with open("lista_canales.txt", "w") as f:
        f.write("\n".join(total))
    
    print(f"\n[!] RESTAURACIÓN COMPLETA: {len(total)} canales con nombre.")
    if len(total) > 0:
        os.system('git add . && git commit -m "Restauración: Agenda + 24/7" && git push origin main')
        print("[+] El botín vuelve a estar seguro en GitHub.")

if __name__ == "__main__":
    ejecucion_final()
