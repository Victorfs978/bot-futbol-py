import requests
import re

# La base de su imperio pirata
URL_PANEL = "https://victorfs.neocities.org/"

def saquear_imperio():
    print(f"🏴‍☠️ INICIANDO SAQUEO EN EL PANEL: {URL_PANEL}")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    try:
        # 1. Entramos al panel principal para ver los 226 links
        respuesta_panel = requests.get(URL_PANEL, headers=headers, timeout=15)
        # Buscamos todos los links que están en los números (ej: canal1.html, etc)
        objetivos = re.findall(r'href=["\'](.[^"\']+)["\']', respuesta_panel.text)
        
        # Filtramos para quedarnos solo con las subpáginas de su Neocities
        paginas_a_escanear = [URL_PANEL + obj for obj in objetivos if obj.endswith('.html') or '/' in obj]
        print(f"🎯 Se detectaron {len(paginas_a_escanear)} objetivos piratas.")

        links_m3u8_finales = []

        # 2. Entramos a cada una de las 226 páginas a robar el stream
        for i, url in enumerate(paginas_a_escanear[:226]):
            try:
                print(f"🕵️ Escaneando objetivo {i+1}: {url}")
                r = requests.get(url, headers=headers, timeout=5)
                # Buscamos el link .m3u8 escondido en el código
                streams = re.findall(r'http[s]?://[^\s"\'<>]+m3u8', r.text)
                
                for s in streams:
                    if s not in links_m3u8_finales:
                        links_m3u8_finales.append(s)
                        print(f"  ✅ SEÑAL CAPTURADA: {s}")
            except:
                continue

        print(f"\n🏆 BOTÍN TOTAL: {len(links_m3u8_finales)} señales capturadas.")
        
    except Exception as e:
        print(f"❌ Error al entrar al panel: {e}")

if __name__ == "__main__":
    saquear_imperio()
    
