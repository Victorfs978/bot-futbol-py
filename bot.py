import asyncio
from playwright.sync_api import sync_playwright
import time

# Los objetivos más calientes
OBJETIVOS = [
    "https://pelotalibretv.su",
    "https://antenasport.top",
    "https://teledeportes.top/stream-tv.php",
    "https://daddyhd.com"
]

def asalto_f12():
    with sync_playwright() as p:
        # Lanzamos un navegador real (Disfrazado de humano)
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        
        botin = []
        
        for url in OBJETIVOS:
            page = context.new_page()
            print(f"🕵️ Explorando como F12 en: {url}")
            
            # Lista para capturar links m3u8 detectados en la red
            links_detectados = []
            
            # Escuchamos el tráfico de red (Igual que el Inspector F12)
            page.on("request", lambda request: links_detectados.append(request.url) if ".m3u8" in request.url else None)
            
            try:
                # Entramos y esperamos a que cargue la "cocina" de la web
                page.goto(url, wait_until="networkidle", timeout=30000)
                time.sleep(5) # Tiempo para que el reproductor se active
                
                if links_detectados:
                    link_final = links_detectados[0]
                    print(f"✅ ¡PRESA CAZADA!: {link_final}")
                    botin.append(f"CANAL_F12|{link_final}")
                else:
                    # Si no hay m3u8, buscamos el iframe para Sketchware
                    iframe = page.query_selector("iframe")
                    if iframe:
                        src = iframe.get_attribute("src")
                        print(f"📦 IFRAME CAPTURADO: {src}")
                        botin.append(f"IFRAME_F12|{src}")
            except Exception as e:
                print(f"❌ Error en asalto: {e}")
            finally:
                page.close()
        
        browser.close()
        
        # Guardar resultados
        with open("lista_canales.txt", "w", encoding='utf-8') as f:
            if botin:
                f.write("\n".join(botin))
            else:
                f.write("ERROR|El navegador invisible no detectó señales. Necesitamos instalar dependencias.")

if __name__ == "__main__":
    asalto_f12()
    
