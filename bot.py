import requests
import re

def asalto_fctv33_blindado():
    base_url = "https://www.fctv33.site"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Referer': base_url,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
    }

    try:
        print(f"🕵️ Intentando romper el cifrado de {base_url}...")
        response = requests.get(base_url, headers=headers, timeout=15)
        
        # 1. Buscamos todas las páginas de canales (las que terminan en .html)
        paginas = re.findall(r'href="(https?://www\.fctv33\.[^/]+/[^"]+\.html)"', response.text)
        paginas_unicas = list(set(paginas))
        
        if not paginas_unicas:
            print("❌ No se encontraron páginas de canales. El sitio cambió su estructura.")
            return

        botin = []
        for pg in paginas_unicas:
            try:
                # 2. Entramos a la página del canal
                res_pg = requests.get(pg, headers=headers, timeout=10)
                
                # 3. TÁCTICA NUEVA: Buscamos el IFRAME o el SCRIPT que carga el player
                # Buscamos fuentes de video típicas que usa FCTV33 (como vood, sfntv, stream, etc.)
                iframe = re.search(r'iframe.*?src="(.*?)"', res_pg.text)
                
                nombre = pg.split('/')[-1].replace('.html', '').replace('-', ' ').upper()

                if iframe:
                    url_iframe = iframe.group(1)
                    # Si el iframe es relativo, le pegamos la base
                    if url_iframe.startswith('//'):
                        url_iframe = 'https:' + url_iframe
                    
                    # Guardamos el link del reproductor (a veces esto es lo único que necesitamos)
                    botin.append(f"{nombre}|{url_iframe}")
                    print(f"✅ CAPTURADO PLAYER: {nombre}")
                
                # Intentamos buscar el m3u8 escondido en scripts
                m3u8_hidden = re.search(r'source:\s*["\'](http.*?m3u8.*?)["\']', res_pg.text)
                if m3u8_hidden:
                    botin.append(f"{nombre}_DIRECTO|{m3u8_hidden.group(1)}")
                    print(f"🔥 CAPTURADO M3U8: {nombre}")

            except:
                continue

        # 4. Generamos el botín para Sketchware
        with open("lista_canales.txt", "w", encoding='utf-8') as f:
            if botin:
                f.write("\n".join(botin))
                print(f"🏁 ASALTO FINALIZADO: {len(botin)} señales en la bolsa.")
            else:
                print("⚠️ El sitio está usando protección por Cookies. Necesitamos otra táctica.")

    except Exception as e:
        print(f"🚫 Error en la conexión: {e}")

if __name__ == "__main__":
    asalto_fctv33_blindado()
            
