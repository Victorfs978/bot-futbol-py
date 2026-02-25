import requests
import re

URL_PANEL = "https://victorfs.neocities.org/"

def saquear_agresivo():
    print(f"🏴‍☠️ INICIANDO ATAQUE DE PRECISIÓN EN: {URL_PANEL}")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Referer': 'https://google.com'
    }
    
    try:
        r_panel = requests.get(URL_PANEL, headers=headers, timeout=15)
        # Extraemos links limpios
        enlaces = re.findall(r'href=["\'](https?://[^"\']+)["\']', r_panel.text)
        objetivos = list(set([e for e in enlaces if "neocities" not in e or e.count("http") == 1]))
        
        print(f"🎯 Objetivos reales a saquear: {len(objetivos)}")
        botin = []

        for i, url in enumerate(objetivos):
            try:
                print(f"🕵️ Saqueando {i+1}/{len(objetivos)}: {url}")
                r = requests.get(url, headers=headers, timeout=10)
                
                # Buscamos m3u8, mp4, o cualquier señal de stream
                streams = re.findall(r'(https?://[^\s"\'<>]+(?:\.m3u8|\.mp4|\.ts|index\.m3u8))', r.text)
                
                if streams:
                    for s in streams:
                        if s not in botin:
                            botin.append(s)
                            print(f"  ✅ ¡LO TENGO!: {s}")
            except:
                continue

        print(f"\n🏆 BOTÍN FINAL: {len(botin)} señales capturadas.")
        
    except Exception as e:
        print(f"❌ Error fatal: {e}")

if __name__ == "__main__":
    saquear_agresivo()
    
