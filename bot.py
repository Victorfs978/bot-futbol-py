import requests
import re

def ataque_fctv33():
    # Usamos el dominio que esté activo
    base_url = "https://www.fctv33.site"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': base_url
    }

    try:
        print(f"📡 Iniciando asalto a {base_url}...")
        response = requests.get(base_url, headers=headers, timeout=15)
        
        # 1. Buscamos todos los links de canales/partidos en la home
        # Buscamos patrones como: href="https://www.fctv33.site/p/canal-1.html"
        links_canales = re.findall(r'href="(https?://www\.fctv33\.[^/]+/[^"]+\.html)"', response.text)
        
        # Limpiamos duplicados
        links_unicos = list(set(links_canales))
        print(f"🔎 Se encontraron {len(links_unicos)} posibles señales.")

        botin_final = []

        for link in links_unicos:
            try:
                # 2. Entramos a cada página de canal
                res_canal = requests.get(link, headers=headers, timeout=10)
                
                # 3. Buscamos el link del reproductor (m3u8) escondido
                # A veces está directo, a veces dentro de un iframe
                m3u8 = re.search(r'["\'](http[^\s"\']+\.m3u8[^\s"\']*)["\']', res_canal.text)
                
                # Extraemos un nombre amigable del link (ej: canal-1)
                nombre = link.split('/')[-1].replace('.html', '').replace('-', ' ').upper()

                if m3u8:
                    botin_final.append(f"{nombre}|{m3u8.group(1)}")
                    print(f"✅ CAPTURADO: {nombre}")
            except:
                continue

        # 4. Guardamos el botín para Sketchware
        with open("lista_canales.txt", "w", encoding='utf-8') as f:
            if botin_final:
                f.write("\n".join(botin_final))
                print(f"🏁 ¡MISIÓN ÉXITOSA! {len(botin_final)} links extraídos automáticamente.")
            else:
                print("❌ No se pudo extraer la señal. El sitio puede tener protección anti-bot.")

    except Exception as e:
        print(f"🚫 Error en el ataque: {e}")

if __name__ == "__main__":
    ataque_fctv33()
    
