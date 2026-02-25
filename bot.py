import requests
import re

def gran_asalto_226():
    print("🚀 INICIANDO EL GRAN ASALTO: BARRIDO DE 226 LINKS DESDE NEOCITIES...")
    
    # URL de su centro de mando
    lista_neocities = "https://victorfs.neocities.org/lista_canales.txt"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'Referer': 'https://streamtp10.com/'
    }

    try:
        # 1. Obtenemos sus 226 objetivos
        r_lista = requests.get(lista_neocities, headers=headers, timeout=15)
        objetivos = re.findall(r'(https?://[^\s"\'<>]+)', r_lista.text)
        print(f"✅ {len(objetivos)} objetivos cargados. ¡Fuego a discreción!")

        botin_final = []

        # 2. Atacamos cada link buscando el 'playbackURL' o el '.m3u8'
        for i, url in enumerate(objetivos):
            if "neocities" in url: continue # Saltamos su propia web
            try:
                print(f"🛰️ Escaneando ({i+1}/{len(objetivos)}): {url}")
                r_web = requests.get(url, headers=headers, timeout=7)
                
                # Buscamos la señal de video con la técnica que nos dio éxito
                video = re.search(r'var\s+playbackURL\s*=\s*["\'](.*?\.m3u8.*?)["\']', r_web.text)
                if not video:
                    video = re.search(r'["\'](https?://.*?\.m3u8.*?)["\']', r_web.text)
                
                if video:
                    enlace = video.group(1)
                    if enlace not in botin_final:
                        botin_final.append(enlace)
                        print(f"  💰 ¡BOTÍN ASEGURADO!")
            except:
                continue

        print("\n" + "X"*50)
        print(f"🏆 MISIÓN CUMPLIDA: {len(botin_final)} CANALES PREMIUM DETECTADOS")
        print("X"*50)
        for canal in botin_final:
            print(f"⚽ {canal}")
        print("X"*50)

    except Exception as e:
        print(f"❌ Error en el centro de mando: {e}")

if __name__ == "__main__":
    gran_asalto_226()
                
