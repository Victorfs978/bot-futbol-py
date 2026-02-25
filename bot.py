import requests
import re

def atacar_streamtp():
    print("🎯 ATACANDO OBJETIVO: STREAMTP10.COM")
    print("📡 BUSCANDO SEÑALES DE ESPN, WIN SPORTS Y TYC...")
    
    url_objetivo = "https://streamtp10.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Referer': 'https://streamtp10.com/',
        'Origin': 'https://streamtp10.com'
    }

    try:
        # 1. Entramos a la página principal
        r = requests.get(url_objetivo, headers=headers, timeout=15)
        
        # 2. Buscamos los "Links" de los canales pesados
        # Estos suelen ser archivos .php o .html que cargan el reproductor
        canales_raw = re.findall(r'href=["\'](.*?\.php\?id=.*?)["\']', r.text)
        
        if not canales_raw:
            # Si no hay PHP, buscamos cualquier enlace que parezca de transmisión
            canales_raw = re.findall(r'window\.open\([\'"](.*?)\',', r.text)

        print(f"🕵️ Detectadas {len(canales_raw)} posibles puertas de entrada...")

        botin_de_guerra = []

        # 3. Entramos a cada canal para pescar el m3u8 real
        for canal_url in canales_raw[:15]: # Analizamos los primeros 15 (donde está lo bueno)
            if not canal_url.startswith('http'):
                canal_url = "https://streamtp10.com/" + canal_url
            
            try:
                print(f"🔍 Analizando canal: {canal_url.split('=')[-1]}")
                res_canal = requests.get(canal_url, headers=headers, timeout=10)
                
                # Buscamos el link m3u8 o el iframe que esconde el video
                m3u8 = re.search(r'source:\s*["\'](.*?\.m3u8.*?)["\']', res_canal.text)
                if not m3u8:
                    m3u8 = re.search(r'file:\s*["\'](.*?\.m3u8.*?)["\']', res_canal.text)
                
                if m3u8:
                    enlace_final = m3u8.group(1)
                    botin_de_guerra.append(enlace_final)
                    print(f"  ✅ ¡LINK CAPTURADO!: {enlace_final}")
            except:
                continue

        print("\n" + "="*50)
        if botin_de_guerra:
            print(f"🏆 SEÑALES DE LIGA CAPTURADAS: {len(botin_de_guerra)}")
            for i, link in enumerate(botin_de_guerra):
                print(f"⚽ CANAL PREMIUM {i+1}: {link}")
        else:
            print("❌ El escudo es fuerte. Los links están protegidos por IFRAMES externos.")
            print("💡 MAÑANA atacaremos los servidores: 'global1.php' y 'global2.php' de esa web.")
        print("="*50)

    except Exception as e:
        print(f"❌ Error al conectar con el objetivo: {e}")

if __name__ == "__main__":
    atacar_streamtp()
    
