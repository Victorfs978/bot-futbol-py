import requests, re, os, concurrent.futures

objetivos = [
    "camel1.live", "antenasport.top", "strumyk.uk", "daddyhd.com", "dlhd.link",
    "teledeportes.top", "deporte-libre.click", "tudeporte.pro", "sosplay.net",
    "bolaloca.my", "rereyano.ru", "sportsbay.dk", "rbsports77.mom", "la14hd.com",
    "rdtvonline.com", "pelotalibretv.su", "vegeta-tv-2.zya.me", "ppv.to",
    "strmd.link", "goluchitas.com", "streamingon.org", "tvporinternet2.com",
    "futbollibre2.com", "telextrema2.com", "sportzx.cc", "ntvstream.cx",
    "sportplus.live", "platinsport.com", "myfootball.pw", "liveball.st",
    "vipleague.lc", "calciostream.help", "rojadirecta.eu", "vipbox.lc"
]

H = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def asalto_objetivo(dominio):
    botin_local = []
    url = f"https://{dominio}"
    try:
        print(f"[*] Atacando: {dominio}...")
        r = requests.get(url, headers=H, timeout=10)
        links = re.findall(r'src=["\'](https?://[^"\']+\.(?:m3u8|mpd|php))["\']', r.text)
        links += re.findall(r'href=["\'](https?://[^"\']+\.(?:m3u8|mpd|php))["\']', r.text)
        for l in set(links):
            nombre = dominio.split('.')[0].upper()
            botin_local.append(f"TOTAL-ATTACK: {nombre}|{l}")
            print(f"[+] CAPTURADO en {dominio}: {l[:40]}")
    except: pass
    return botin_local

def ejecucion_maxima():
    print("🔥 INICIANDO ASALTO MASIVO A TODA LA RED...")
    botin_total = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        resultados = list(executor.map(asalto_objetivo, objetivos))
    for r in resultados:
        botin_total.extend(r)
    with open("lista_canales.txt", "w") as f:
        f.write("\n".join(botin_total))
    print(f"\n[!] ASALTO COMPLETADO: {len(botin_total)} canales robados.")
    if len(botin_total) > 0:
        os.system('git add . && git commit -m "Ataque Masivo Total" && git push origin main')
        print("[+] Botín asegurado en GitHub.")

if __name__ == "__main__":
    ejecucion_maxima()
