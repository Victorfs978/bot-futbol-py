import requests
import re

def infiltracion_futbol():
    print("🕵️ INICIANDO OPERACIÓN INFILTRACIÓN: BUSCANDO PECES GORDOS...")
    
    # Aquí atacamos directamente donde suelen esconderse los streams de liga
    objetivos = [
        "https://victorfs.neocities.org/", # Su panel de 226 páginas
        "https://raw.githubusercontent.com/m3u8playlist/Free-TV/main/playlist.m3u8"
    ]
    
    # Fingimos que somos un iPhone para que la web nos suelte el stream más fácil
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1',
        'Accept': '*/*',
        'Referer': 'https://google.com/'
    }

    botin_real = []

    for url in objetivos:
        try:
            print(f"🚀 Atacando fuente: {url}")
            r = requests.get(url, headers=headers, timeout=15)
            
            # Buscamos links m3u8 que tengan palabras clave de fútbol premium
            # Buscamos patrones de servidores que suelen tener ESPN, FOX, etc.
            enlaces = re.findall(r'(https?://[^\s"\'<>]+m3u8[^\s"\'<>]*)', r.text)
            
            for l in enlaces:
                l_low = l.lower()
                # Filtro agresivo: Solo nos interesan los que huelan a deporte importante
                if any(x in l_low for x in ['espn', 'fox', 'win', 'tnt', 'vix', 'starplus', 'directv', 'sky', 'liga']):
                    if l not in botin_real:
                        botin_real.append(l)
                        print(f"  ✅ ¡PEZ GORDO DETECTADO!: {l}")
        except:
            continue

    print("\n" + "="*50)
    if botin_real:
        print(f"🏆 SEÑALES PREMIUM ENCONTRADAS: {len(botin_real)}")
        for i, link in enumerate(botin_real):
            print(f"⚽ LIVE {i+1}: {link}")
    else:
        print("❌ Las páginas están blindadas. Necesitamos atacar los IFRAMES directamente.")
        print("💡 CONSEJO: Pásame el link de UNA sola página de esas 226 que tú sepas que funciona bien.")
    print("="*50)

if __name__ == "__main__":
    infiltracion_futbol()
    
