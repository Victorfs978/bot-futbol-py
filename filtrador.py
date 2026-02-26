import re

lista_gigante = """
[PEGA AQUÍ TU LISTA DE 223 LINKS SI QUIERES FILTRARLA O USAREMOS LA INTERNA]
"""

# Lista de dominios que ya dominamos
dominados = ['castmedia.click', 'livetv.sx', 'antenasport.top', 'streamtp10.com']

# Extraer dominios únicos de tu lista
urls = re.findall(r'https?://(?:www\.)?([^/\s]+)', """
1 camel1.live 2 antenasport.top 3 strumyk.uk 4 daddyhd.com 5 dlhd.link 
9 teledeportes.top 12 deporte-libre.click 23 tudeporte.pro 26 sosplay.net 
31 bolaloca.my 32 rereyano.ru 33 sportsbay.dk 38 la14hd.com 39 rdtvonline.com
95 pelotalibretv.su 99 vegeta-tv-2.zya.me 156 ppv.to 189 strmd.link 190 goluchitas.com
197 ntvstream.cx 198 sportplus.live 201 platinsport.com 203 myfootball.pw
""")

unicos = sorted(list(set(urls)))
finales = [u for u in unicos if u not in dominados]

print(f"[*] Se detectaron {len(finales)} objetivos nuevos y únicos.")
print("[!] Objetivos prioritarios para señales 24/7:")
for i, dom en enumerate(finales[:10], 1):
    print(f"    {i}. {dom}")
