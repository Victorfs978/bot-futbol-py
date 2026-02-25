import requests
import re

def ataque_desde_neocities():
    print("📡 CONECTANDO A SU ALOJAMIENTO EN NEOCITIES...")
    
    # 1. URL de su lista maestra en Neocities
    url_maestra = "https://victorfs.neocities.org/lista_canales.txt" # <--- Asegúrese de que este sea el nombre de su archivo
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36'
    }

    try:
        # 2. Descargamos sus 226 links
        r_maestra = requests.get(url_maestra, headers=headers, timeout=15)
        mis_objetivos = re.findall(r'(https?://[^\s"\'<>]+)', r_maestra.text)
        
        print(f"✅ Se detectaron {len(mis_objetivos)} links en su Neocities. Iniciando infiltración...")

        botin_final = []

        # 3. Entramos a cada uno de los 226 links
        for i, link in enumerate(mis_objetivos):
            try:
                # Solo atacamos links que no sean de Neocities para no entrar en bucle
                if "neocities.org" in link: continue
                
                print(f"🚀 Escaneando ({i+1}/{len(mis_objetivos)}): {link}")
                r_web = requests.get(link, headers=headers, timeout=8)
                
                # Aplicamos la fórmula del éxito: buscar el playbackURL o el m3u8 con token
                encontrado = re.search(r'["\'](https?://.*?\.m3u8.*?)["\']', r_web.text)
                
                if encontrado:
                    link_vivo = encontrado.group(1)
                    if link_vivo not in botin_final:
                        botin_final.append(link_vivo)
                        print(f"  ⭐ ¡CANAL ENCONTRADO EN {link}!")
            except:
                continue

        print("\n" + "="*50)
        print(f"🏆 RESULTADO: {len(botin_final)} CANALES LISTOS PARA LA APP")
        print("="*50)
        for canal in botin_final:
            print(f"⚽ {canal}")
        print("="*50)

    except Exception as e:
        print(f"❌ Error al conectar con Neocities: {e}")

if __name__ == "__main__":
    ataque_desde_neocities()
    
