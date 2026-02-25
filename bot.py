import requests
import re
import time

URL_PANEL = "https://victorfs.neocities.org/"

def cazar_en_profundidad():
    print(f"🕵️ ESCANEO PROFUNDO ACTIVADO EN: {URL_PANEL}")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': 'https://www.google.com/'
    }

    try:
        # 1. Obtenemos las 226 páginas
        r_panel = requests.get(URL_PANEL, headers=headers, timeout=15)
        enlaces = re.findall(r'href=["\'](https?://[^"\']+)["\']', r_panel.text)
        objetivos = list(set([e for e in enlaces if "neocities" not in e or e.count("http") == 1]))
        
        print(f"🎯 Atacando {len(objetivos)} webs de fútbol...")
        botin = []

        for i, url in enumerate(objetivos):
            try:
                print(f"🚀 Entrando a objetivo {i+1}: {url}")
                # Esperamos 1 segundo para no ser bloqueados
                time.sleep(1)
                res = requests.get(url, headers=headers, timeout=10)
                
                # BUSQUEDA NIVEL 1: Links directos m3u8
                found = re.findall(r'["\'](https?://[^\s"\'<>]+m3u8[^\s"\'<>]*)["\']', res.text)
                
                # BUSQUEDA NIVEL 2: Links dentro de scripts (reproductores)
                if not found:
                    found = re.findall(r'source:\s*["\'](https?://[^"\']+)["\']', res.text)
                
                # BUSQUEDA NIVEL 3: IFRAMES (donde se esconde el canal)
                if not found:
                    iframes = re.findall(r'iframe.+src=["\'](https?://[^"\']+)["\']', res.text)
                    for frame_url in iframes[:2]: # Solo los 2 primeros frames
                        print(f"   ⚓ Siguiendo rastro en Frame...")
                        r_frame = requests.get(frame_url, headers=headers, timeout=5)
                        found += re.findall(r'(https?://[^\s"\'<>]+m3u8)', r_frame.text)

                for s in found:
                    if s not in botin:
                        botin.append(s)
                        print(f"  ✅ ¡CAPTURADO!: {s}")
            except:
                continue

        print(f"\n🏆 RESUMEN DEL SAQUEO: {len(botin)} links para la App.")
        
    except Exception as e:
        print(f"❌ Error en el panel: {e}")

if __name__ == "__main__":
    cazar_en_profundidad()
        
    
