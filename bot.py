import requests
import re

def ataque_stream2watch():
    print("🦅 INICIANDO OPERACIÓN OJO DE HALCÓN: OBJETIVO STREAM2WATCH.PK")
    
    url_base = "https://stream2watch.pk/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': 'https://stream2watch.pk/',
        'Accept-Language': 'es-ES,es;q=0.9'
    }

    try:
        print("🛰️ Escaneando lista de canales internacionales...")
        r = requests.get(url_base, headers=headers, timeout=15)
        
        # 1. Capturamos los enlaces de las páginas de cada canal
        # Buscamos patrones como /video/canal-nombre
        canales_paginas = re.findall(r'href=["\'](https?://stream2watch\.pk/video/[^\s"\'<>]+)["\']', r.text)
        
        if not canales_paginas:
            # Intento alternativo si los links son relativos
            canales_paginas = re.findall(r'href=["\'](/video/[^\s"\'<>]+)["\']', r.text)
            canales_paginas = ["https://stream2watch.pk" + c for c in canales_paginas]

        print(f"✅ Se detectaron {len(canales_paginas)} canales potenciales.")

        botin_premium = []

        # 2. Entramos a los primeros 20 (donde suelen estar los DAZN y beIN)
        for i, url_canal in enumerate(canales_paginas[:20]):
            try:
                nombre_canal = url_canal.split('/')[-1]
                print(f"🔍 Analizando: {nombre_canal}...")
                
                r_canal = requests.get(url_canal, headers=headers, timeout=10)
                
                # Buscamos la 'joya': el iframe o el link m3u8 escondido
                # Estas webs suelen usar 'source', 'file' o 'url' en scripts
                stream = re.search(r'["\'](https?://.*?\.m3u8.*?)["\']', r_canal.text)
                
                if stream:
                    enlace = stream.group(1)
                    botin_premium.append(f"{nombre_canal.upper()}: {enlace}")
                    print(f"  ⚽ ¡ENCONTRADO!: {nombre_canal}")
                else:
                    # Si no hay m3u8, buscamos el servidor de video (iframe)
                    iframe = re.search(r'iframe.*?src=["\'](https?://.*?)["\']', r_canal.text)
                    if iframe:
                        botin_premium.append(f"{nombre_canal.upper()} (IFRAME): {iframe.group(1)}")
                        print(f"  📺 IFRAME DETECTADO: {nombre_canal}")
            except:
                continue

        print("\n" + "="*50)
        if botin_premium:
            print(f"🏆 BOTÍN INTERNACIONAL: {len(botin_premium)} CANALES")
            for item in botin_premium:
                print(item)
        else:
            print("🚨 El sitio usa protección 'Anti-Bot'.")
            print("💡 TIP: Mañana usaremos un simulador de clic para este sitio.")
        print("="*50)

    except Exception as e:
        print(f"❌ Error de conexión: {e}")

if __name__ == "__main__":
    ataque_stream2watch()
    
