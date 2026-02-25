import requests
import re

def enviar_a_pastebin():
    print("📡 CAZANDO LOS 1500 LINKS DE FÚTBOL...")
    fuentes = [
        "https://iptv-org.github.io/iptv/languages/spa.m3u",
        "https://raw.githubusercontent.com/Guydun/Tv-online/main/Tv-online.m3u",
        "https://raw.githubusercontent.com/TheRealSanjeev/IPTV/main/Global/Sports.m3u"
    ]
    
    todos_los_links = []
    for url in fuentes:
        try:
            r = requests.get(url, timeout=15)
            enlaces = re.findall(r'(https?://[^\s"\'<>]+m3u8)', r.text)
            for l in enlaces:
                if l not in todos_los_links:
                    todos_los_links.append(l)
        except:
            continue

    contenido = f"--- LISTA DE {len(todos_links)} CANALES ---\n\n"
    contenido += "\n".join([f"CANAL {i+1}: {l}" for i, l in enumerate(todos_los_links)])

    print(f"✅ {len(todos_los_links)} links listos. Subiendo a Pastebin...")

    # 🚀 SUBIDA PÚBLICA (Sin cuentas ni basura)
    try:
        data = {
            'api_option': 'paste',
            'api_dev_key': '3662d98045f096752718e88e70396417', # Llave genérica
            'api_paste_code': contenido,
            'api_paste_name': 'Lista_Futbol_Victor',
            'api_paste_format': 'text',
            'api_paste_expire_date': '1D'
        }
        res = requests.post("https://pastebin.com/api/api_post.php", data=data)
        
        if "https://pastebin.com" in res.text:
            print(f"🏆 ¡LO LOGRAMOS! Mira todos tus links aquí:")
            print(f"👉 {res.text}")
        else:
            print(f"❌ Error: {res.text}")
    except Exception as e:
        print(f"❌ Fallo total: {e}")

if __name__ == "__main__":
    enviar_a_pastebin()
    
    
