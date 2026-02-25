import requests
from concurrent.futures import ThreadPoolExecutor

# --- PEGA AQUÍ TU LISTA GIGANTE ---
CANALES_A_PROBAR = """
TVS Sports Bureau (720p)|https://rpn.bozztv.com/gusa/gusa-tvssportsbureau/index.m3u8
NHRA TV (720p)|https://aegis-cloudfront-1.tubi.video/b8c5eb48-349b-454f-9625-63911ee923f5/playlist.m3u8
Golf Network (540p)|http://202.60.106.14:8080/1335/playlist.m3u8
Pac 12 Insider|https://pac12-firetv.amagi.tv/playlist.m3u8
BeIN SPORTS XTRA en Espanol (720p) [Geo-blocked]|https://bein-esp-klowdtv.amagi.tv/playlist.m3u8
""" # ... Pega todos los que faltan aquí

def verificar_canal(linea):
    if "|" not in linea:
        return None
    
    nombre, url = linea.split("|")
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        # Hacemos una petición rápida (timeout de 5 segundos)
        # Usamos stream=True para no descargar todo el video, solo ver si abre
        response = requests.get(url, headers=headers, timeout=5, stream=True)
        
        if response.status_code == 200:
            print(f"✅ FUNCIONA: {nombre}")
            return linea
        else:
            print(f"❌ CAÍDO ({response.status_code}): {nombre}")
            return None
    except:
        print(f"🚫 ERROR DE CONEXIÓN: {nombre}")
        return None

def limpiar_lista():
    lineas = CANALES_A_PROBAR.strip().split('\n')
    print(f"🕵️ Iniciando inspección de {len(lineas)} canales...")
    
    # Usamos 20 hilos para que la revisión sea ultra rápida
    with ThreadPoolExecutor(max_workers=20) as executor:
        resultados = list(executor.map(verificar_canal, lineas))
    
    # Filtramos solo los que devolvieron el link (los que funcionan)
    canales_vivos = [r for r in resultados if r is not None]
    
    with open("lista_canales.txt", "w", encoding='utf-8') as f:
        f.write("\n".join(canales_vivos))
    
    print(f"\n🏁 INFORME FINAL:")
    print(f"📊 Total revisados: {len(lineas)}")
    print(f"🟢 Canales operativos: {len(canales_vivos)}")
    print(f"🔴 Canales eliminados: {len(lineas) - len(canales_vivos)}")

if __name__ == "__main__":
    limpiar_lista()
    
