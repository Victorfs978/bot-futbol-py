import requests
import re
import base64
from concurrent.futures import ThreadPoolExecutor

# --- CENTRO DE MANDO: 226 OBJETIVOS CARGADOS ---
OBJETIVOS = [
    "https://www.camel1.live", "https://antenasport.top", "https://strumyk.uk", "https://daddyhd.com", "https://dlhd.link",
    "https://teledeportes.top/stream-tv.php", "https://tudeporte.pro", "https://nowevents.xyz", "https://sosplay.net",
    "https://deporte-libre.click/", "https://pelotalibretv.su", "https://la14hd.com", "https://streameast100.is",
    "https://totalsportek.army", "https://www.footybite.to", "https://vipleague.im", "https://hesgoal-tv.io",
    "https://rojadirectatv.me", "https://pirlotv.online", "https://tarjetaroja.me", "https://futbollibre.lol",
    "https://megadeportes.live", "https://pirlotvonline.org", "https://lateletuya.com", "https://intergoles.top",
    "https://verliga.com", "https://zonadeportes.tv", "https://elitestream.it", "https://ustvgo.tv", "https://123tvnow.com",
    "https://stream2watch.sx", "https://cricfree.io", "https://batmanstream.org", "https://mamahd.best", "https://viprow.me",
    "https://strikeout.nu", "https://sportrar.tv", "https://livesoccertv.com", "https://scorebat.com", "https://footyroom.com",
    "https://fullmatchtv.com", "https://matchat.online", "https://rojadirectaonline.com", "https://pirlotvlive.com",
    "https://tarjetarojatv.online", "https://futbolenvivo.com", "https://verfutbol.online", "https://deportestv.online",
    "https://todofutbol.online", "https://canalesdetv.online", "https://tvpuntos.online", "https://teledirecto.online",
    "https://verlatv.online", "https://mitele.online", "https://rtve.online", "https://telecinco.online", "https://antena3.online",
    "https://lasexta.online", "https://cuatro.online", "https://teledeporte.online", "https://fdf.online", "https://divinity.online",
    "https://energy.online", "https://bemad.online", "https://boing.online", "https://neox.online", "https://nova.online",
    "https://mega.online", "https://atreseries.online", "https://ten.online", "https://trece.online", "https://dkiss.online",
    "https://dmax.online", "https://paramount.online", "https://disney.online", "https://clan.online", "https://boing.online",
    "https://24h.online", "https://tve1.online", "https://tve2.online", "https://canalplus.online", "https://movistarplus.online",
    "https://bein.online", "https://eurosport.online", "https://dazn.online", "https://skysports.online", "https://btsport.online",
    "https://foxsports.online", "https://espn.online", "https://tycsports.online", "https://win-sports.online", "https://tigosports.online",
    "https://directv.online", "https://clarosports.online", "https://azteca.online", "https://televisa.online", "https://tnt.online",
    "https://hbo.online", "https://showtime.online", "https://starz.online", "https://epix.online", "https://amc.online",
    "https://fx.online", "https://usa.online", "https://syfy.online", "https://tnt.online", "https://tbs.online", "https://tru.online",
    "https://cnn.online", "https://msnbc.online", "https://foxnews.online", "https://bbc.online", "https://aljazeera.online",
    "https://rt.online", "https://france24.online", "https://dw.online", "https://euronews.online", "https://nhk.online",
    "https://cgtn.online", "https://tve.online", "https://antena3.online", "https://telecinco.online", "https://lasexta.online",
    "https://cuatro.online", "https://tve2.online", "https://teledeporte.online", "https://24h.online", "https://clan.online",
    "https://neox.online", "https://nova.online", "https://mega.online", "https://atreseries.online", "https://fdf.online",
    "https://energy.online", "https://divinity.online", "https://bemad.online", "https://boing.online", "https://paramount.online",
    "https://mtv.online", "https://comedycentral.online", "https://nick.online", "https://disney.online", "https://disneyjr.online",
    "https://disneyxd.online", "https://discovery.online", "https://natgeo.online", "https://history.online", "https://odisea.online",
    "https://viajar.online", "https://cocina.online", "https://decasa.online", "https://hollywood.online", "https://tcm.online",
    "https://sundance.online", "https://dark.online", "https://xtrm.online", "https://somos.online", "https://8tv.online",
    "https://tv3.online", "https://324.online", "https://esport3.online", "https://sx3.online", "https://33.online",
    "https://etb.online", "https://etb2.online", "https://etb3.online", "https://etb4.online", "https://tvg.online",
    "https://tvg2.online", "https://tvg3.online", "https://telemadrid.online", "https://laotra.online", "https://canalsur.online",
    "https://canalsur2.online", "https://andalucia.online", "https://aragontv.online", "https://rtpa.online", "https://rtvcyf.online",
    "https://rtvm.online", "https://rtvv.online", "https://rtvcm.online", "https://rtvcanarias.online", "https://rtvextremadura.online",
    "https://rtvib.online", "https://rtvmurcia.online", "https://rtvrioja.online", "https://rtvnavarra.online", "https://rtvceuta.online",
    "https://rtvmelilla.online", "https://rtvmadrid.online", "https://rtvcatalunya.online", "https://rtveuskadi.online",
    "https://rtvgalicia.online", "https://rtvandalucia.online", "https://rtvaragon.online", "https://rtvasturias.online",
    "https://rtvbaleares.online", "https://rtvcanarias.online", "https://rtvcastilla.online", "https://rtvlamancha.online",
    "https://rtvmurcia.online", "https://rtvnavarra.online", "https://rtvrioja.online", "https://rtvvalencia.online",
    "https://rtvceuta.online", "https://rtvmelilla.online"
]

def obtener_proxys():
    try:
        r = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all", timeout=10)
        return r.text.strip().split('\r\n')
    except: return []

def desarmar_sitio(url, proxy=None):
    headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1', 'Referer': url}
    pxs = {'http': f'http://{proxy}', 'https': f'http://{proxy}'} if proxy else None
    try:
        r = requests.get(url, headers=headers, proxies=pxs, timeout=12)
        h = r.text
        m = re.search(r'["\'](https?://[^\s\'"]+\.m3u8[^\s\'"]*)["\']', h)
        if m: return m.group(1).replace('\\/', '/')
        i = re.search(r'<iframe.*?src=["\']([^"\']+)["\']', h)
        if i:
            l = i.group(1)
            if l.startswith('//'): l = "https:" + l
            return l
        b = re.findall(r'["\']([A-Za-z0-9+/]{40,})={0,2}["\']', h)
        for x in b:
            try:
                d = base64.b64decode(x).decode('utf-8')
                if ".m3u8" in d: return d
            except: continue
    except: return None
    return None

def ejecutar_ataque_total():
    pxs = obtener_proxys()
    botin = []
    with ThreadPoolExecutor(max_workers=25) as executor:
        tareas = [executor.submit(desarmar_sitio, url, pxs[i % len(pxs)] if pxs else None) for i, url in enumerate(OBJETIVOS)]
        for i, t in enumerate(tareas):
            res = t.result()
            if res:
                botin.append(f"CANAL_{i+1}|{res}")
                print(f"✅ CAPTURADO: {i+1}")
    with open("lista_canales.txt", "w", encoding='utf-8') as f:
        f.write("\n".join(botin) if botin else "ERROR|Ataque bloqueado")
    print(f"🏁 ASALTO TERMINADO: {len(botin)} presas.")

if __name__ == "__main__":
    ejecutar_ataque_total()
    
