import requests
import re

URL_PANEL = "https://victorfs.neocities.org/"

def saquear_imperio():
    print(f"🏴‍☠️ INICIANDO SAQUEO LIMPIO EN: {URL_PANEL}")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    try:
        r_panel = requests.get(URL_PANEL, headers=headers, timeout=15)
        # 1. Buscamos los links reales que están detrás de sus números
        enlaces_sucios = re.findall(r'href=["\'](https?://[^"\']+)["\']', r_panel.text)
        
        # Limpiamos para que no se duplique el neocities.org
        objetivos = list(set(enlaces_sucios)) 
        print(f"🎯 Se detectaron {len(objetivos)} objetivos piratas REALES.")

        links_m3u8_finales = []

        # 2. Atacamos cada web pirata de verdad
        for i, url in enumerate(objetivos):
            try:
                print(f"🕵️ Saqueando objetivo {i+1}: {url}")
                r = requests.get(url, headers=headers, timeout=8)
                # Buscamos el stream m3u8
                streams = re.findall(r'http[s]?://[^\s"\'<>]+m3u8', r.text)
                
                for s in streams:
                    if s not in links_m3u8_finales:
                        links_m3u8_finales.append(s)
                        print(f"  ✅ SEÑAL CAPTURADA: {s}")
            except:
                continue

        print(f"\n🏆 BOTÍN FINAL: {len(links_m3u8_finales)} señales capturadas.")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    saquear_imperio()
    
    
