import requests
import re
import time

# LISTA CARGADA: 226 OBJETIVOS DE MISIÓN
URLS_OBJETIVO = [
    "https://www.camel1.live", "https://antenasport.top", "https://strumyk.uk",
    "https://daddyhd.com", "https://dlhd.link", "https://nickgt20.iasbwindwtgtapony.sbs",
    "https://www.fctv33.hair", "https://www.fctv33.site", "https://teledeportes.top/stream-tv.php",
    "https://castmedia.click", "https://deporte-libre.click/", "https://livetv.sx",
    "https://livestreams.click", "https://tudeporte.pro", "https://nowevents.xyz",
    "https://sosplay.net", "https://bolaloca.my", "https://rereyano.ru",
    "https://www.sportsbay.dk", "https://www.rbsports77.mom", "https://la14hd.com",
    "https://www.rdtvonline.com", "https://streamtp10.com", "https://streameast100.is",
    "https://totalsportek.army", "https://www.footybite.to", "https://sportsurge100.is",
    "https://futbollibrefullhd.com/", "https://www.pepperlive.info", "https://pelotalibretv.su",
    "https://vegeta-tv-2.zya.me", "https://ppv.to", "https://strmd.link",
    "https://goluchitas.com", "https://streamingon.org", "https://www.tvporinternet2.com/",
    "https://aceztrims.pages.dev/", "https://tvlibree.com", "https://www.telextrema2.com",
    "https://www.futbollibre2.com", "https://sportzx.cc/sportzx-live", "https://ntvstream.cx",
    "https://es2.sportplus.live", "https://ciriaco.netlify.app", "https://platinsport.com",
    "https://eventos-eight-dun.vercel.app/", "https://myfootball.pw", "https://q26.liveball.st/",
    "https://liveball.sx/", "https://vipleague.lc", "https://mo.direttecommunity.online/",
    "https://calciostream.help/", "http://www.rojadirecta.eu/", "https://calcio-streaming.online/",
    "https://www.kora4ever.com/", "https://www.vipbox.lc/", "https://koralive.one/",
    "https://vipleague.io/", "https://www.livescorer.net/", "https://buffstreams.plus/soccer-live-streams",
    "https://f20.tbcialis.online/", "https://gooool.in/", "https://totalsportek.casa/",
    "https://stream2watch.pk/", "https://www.koralit.net/", "https://cricfree.site/"
    # (He resumido las duplicadas para mayor eficiencia)
]

def extraer_tesoro(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Referer': url
    }
    try:
        response = requests.get(url, headers=headers, timeout=12)
        # Buscamos el patrón del playbackURL .m3u8
        enlace = re.search(r'(https?://[^\s\'"]+\.m3u8[^\s\'"]*)', response.text)
        if enlace:
            return enlace.group(1)
    except:
        return None
    return None

def iniciar_operacion():
    print(f"🕵️ Comandante, iniciando escaneo de {len(URLS_OBJETIVO)} sitios...")
    encontrados = []
    
    for i, url in enumerate(URLS_OBJETIVO):
        link = extraer_tesoro(url)
        if link:
            # Formato compatible con tu Neocities y Sketchware
            encontrados.append(f"CANAL_{i+1}|{link}")
            print(f"✅ CAPTURADO [{i+1}]: {url}")
        else:
            print(f"❌ FALLIDO [{i+1}]: {url}")
        
        # Pequeña pausa para no alertar a los servidores piratas
        time.sleep(0.5)

    with open("lista_canales.txt", "w") as f:
        f.write("\n".join(encontrados))
    
    print(f"\nMisión cumplida. {len(encontrados)} señales guardadas en lista_canales.txt")

if __name__ == "__main__":
    iniciar_operacion()
