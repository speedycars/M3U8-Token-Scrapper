from seleniumwire import webdriver
from selenium.webdriver.common.by import By
import configparser
import ast
import pathlib
import requests
import time

config_path = pathlib.Path(__file__).parent.absolute() / "config" / "config.cfg"
config = configparser.ConfigParser()
config.read(config_path, encoding='utf-8')

m3ufilepath = ast.literal_eval(config.get('CONFIG', 'm3ufilepath'))
threadfin_server = ast.literal_eval(config.get('CONFIG', 'threadfin_server'))
bnt1_link = str(config.get('CONFIG', 'bnt1_link'))
dwnews_link = str(config.get('CONFIG', 'dwnews_link'))
aljazeera_link = str(config.get('CONFIG', 'aljazeera_link'))
agrotv_link = str(config.get('CONFIG', 'agrotv_link'))
tv1_link = str(config.get('CONFIG', 'tv1_link'))
bnt2_link = str(config.get('CONFIG', 'bnt2_link'))
bnt3_link = str(config.get('CONFIG', 'bnt3_link'))
bnt4_link = str(config.get('CONFIG', 'bnt4_link'))
sto_auto_moto_link = str(config.get('CONFIG', 'sto_auto_moto_link'))
traveltv_link = str(config.get('CONFIG', 'traveltv_link'))
thisisbg_link = str(config.get('CONFIG', 'thisisbg_link'))
thevoice_link = str(config.get('CONFIG', 'thevoice_link'))
citytv_link = str(config.get('CONFIG', 'citytv_link'))
magictv_link = str(config.get('CONFIG', 'magictv_link'))
darikradio_link = str(config.get('CONFIG', 'darikradio_link'))
radiovitosha_link = str(config.get('CONFIG', 'radiovitosha_link'))
radiohorizont_link = str(config.get('CONFIG', 'radiohorizont_link'))
radiohristobotev_link = str(config.get('CONFIG', 'radiohristobotev_link'))
radiosofia_link = str(config.get('CONFIG', 'radiosofia_link'))
radio1_link = str(config.get('CONFIG', 'radio1_link'))
radio1rock_link = str(config.get('CONFIG', 'radio1rock_link'))
radiozrock_link = str(config.get('CONFIG', 'radiozrock_link'))
tangramegarock_link = str(config.get('CONFIG', 'tangramegarock_link'))
avtoradio_link = str(config.get('CONFIG', 'avtoradio_link'))
bgradio_link = str(config.get('CONFIG', 'bgradio_link'))
btvradio_link = str(config.get('CONFIG', 'btvradio_link'))
radionjoy_link = str(config.get('CONFIG', 'radionjoy_link'))
radioenergy_link = str(config.get('CONFIG', 'radioenergy_link'))
radiofmplus_link = str(config.get('CONFIG', 'radiofmplus_link'))
radiofocus_link = str(config.get('CONFIG', 'radiofocus_link'))
radiofresh_link = str(config.get('CONFIG', 'radiofresh_link'))


options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--autoplay-policy=no-user-gesture-required")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--mute-audio")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("log-level=3") # disable logs
options.add_argument('--disable-search-engine-choice-screen')
options.add_argument('--disable-gpu')
options.add_argument("--disable-cache")
options.add_argument("--disable-crash-reporter")
options.add_argument("--no-crash-upload")
options.add_argument('--incognito')
options.add_argument('--enable-unsafe-swiftshader')



sources = [
    "https://btvplus.bg/live/",
    "https://nova.bg/live",
    "https://nova.bg/live/news",
    "https://euronews.bg/euronews-na-zhivo/",
    "https://www.bgonair.bg/tvonline",
    "https://www.bloombergtv.bg/video",
    "https://iptv-bg.com/btv-comedy-online/",
    "https://iptv-bg.com/btv-action/",
    "https://iptv-bg.com/btv-cinema-online/",
    "https://iptv-bg.com/fox-life-online/",
    "https://iptv-bg.com/fox-crime-online/",
    "https://iptv-bg.com/kino-nova-online/",
    "https://iptv-bg.com/axn-online/",
    "https://iptv-bg.com/viasat-explorer-online/",
    "https://iptv-bg.com/tlc-online/",
    "https://iptv-bg.com/discovery-channel-online/",
    "https://iptv-bg.com/nat-geo-online/",
    "https://iptv-bg.com/nat-geo-wild-online/",
    "https://iptv-bg.com/nova-sport-online/",
    "https://iptv-bg.com/ring-bg-online/"
]
url_list = []

for source in sources:
    driver = webdriver.Chrome(options=options)
    del driver.requests
    driver.set_window_size(1280, 720)
    driver.delete_all_cookies()
    driver.get(source)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    if "btvplus" in source:
        element = driver.find_element("xpath", '//*[@id="preroll-player-wrapper"]/div[2]/div/button[1]')
        element.click()
        time.sleep(2)

    for request in driver.requests:
        if "m3u8" in request.url:
            print(request.url)
            url_list.append(request.url)
            break
    driver.close()
driver.quit()

extm3u = '''#EXTM3U x-tvg-url="https://www.open-epg.com/files/bulgaria1.xml"
'''
bnt1 = '''#EXTINF:-1 tvg-id="БНТ1.bg" tvg-name="БНТ 1 HD" tvg-logo="http://logos.epg.cloudns.org/bnt1.png",БНТ 1 HD
'''+bnt1_link+'''
'''
btv = '''#EXTINF:-1 tvg-id="bTV.bg" tvg-name="bTV HD" tvg-logo="http://logos.epg.cloudns.org/btv.png",bTV HD
'''
nova = '''#EXTINF:-1 tvg-id="Нова телевизия.bg" tvg-name="Nova HD" tvg-logo="http://logos.epg.cloudns.org/nova.png",Nova HD
'''
nova_news = '''#EXTINF:-1 tvg-id="NOVANEWS.bg" tvg-name="Nova News HD" tvg-logo="http://logos.epg.cloudns.org/novanews.png",Nova News HD
'''
euronews = '''#EXTINF:-1 tvg-id="Европа.bg" tvg-name="Euronews Bulgaria" tvg-logo="http://logos.epg.cloudns.org/euronews.png",Euronews Bulgaria
'''
bgonair = '''#EXTINF:-1 tvg-id="България он еър.bg" tvg-name="Bulgaria On Air" tvg-logo="http://logos.epg.cloudns.org/bulgariaonair.png",Bulgaria On Air
'''
bloomberg = '''#EXTINF:-1 tvg-id="Bloomberg TV Bulgaria.bg" tvg-name="Bloomberg TV Bulgaria" tvg-logo="http://logos.epg.cloudns.org/bloomberg.png",Bloomberg TV Bulgaria
'''
btvcomedy = '''#EXTINF:-1 tvg-id="bTV Comedy.bg" tvg-name="bTV Comedy" tvg-logo="http://epg.cloudns.org/tv/logos/btvcomedy.png",bTV Comedy
'''
btvaction = '''#EXTINF:-1 tvg-id="bTV Action.bg" tvg-name="bTV Action" tvg-logo="http://epg.cloudns.org/tv/logos/btvaction.png",bTV Action
'''
btvcinema = '''#EXTINF:-1 tvg-id="bTV Cinema.bg" tvg-name="bTV Cinema" tvg-logo="http://epg.cloudns.org/tv/logos/btvcinema.png",bTV Cinema
'''
starlife = '''#EXTINF:-1 tvg-id="StarLife.bg" tvg-name="Star Life" tvg-logo="http://epg.cloudns.org/tv/logos/starlife.png",Star Life
'''
starcrime = '''#EXTINF:-1 tvg-id="StarCrime.bg" tvg-name="Star Crime" tvg-logo="http://epg.cloudns.org/tv/logos/starcrime.png",Star Crime
'''
kinonova = '''#EXTINF:-1 tvg-id="KinoNova.bg" tvg-name="Kino Nova" tvg-logo="http://epg.cloudns.org/tv/logos/kinonova.png",Kino Nova
'''
axn = '''#EXTINF:-1 tvg-id="AXN.bg" tvg-name="AXN" tvg-logo="https://github.com/harrygg/EPG/blob/master/logos/axn.png?raw=true",AXN
'''
viasatexplorer = '''#EXTINF:-1 tvg-id="Viasat Explorer.bg" tvg-name="Viasat Explorer" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/c/c3/Viasat_Explore-logo.svg",Viasat Explorer
'''
tlc = '''#EXTINF:-1 tvg-id="TLC Balkans.bg" tvg-name="TLC" tvg-logo="https://github.com/harrygg/EPG/blob/master/logos/tlc.png?raw=true",TLC
'''
discovery = '''#EXTINF:-1 tvg-id="Discovery Channel.bg" tvg-name="Discovery Channel" tvg-logo="https://github.com/harrygg/EPG/blob/master/logos/discoveryit.png?raw=true",Discovery Channel
'''
natgeo = '''#EXTINF:-1 tvg-id="National Geographic Channel.bg" tvg-name="National Geographic" tvg-logo="http://epg.cloudns.org/tv/logos/natgeo.png",National Geographic
'''
natgeowild = '''#EXTINF:-1 tvg-id="Nat Geo Wild.bg" tvg-name="National Geographic Wild" tvg-logo="https://github.com/harrygg/EPG/blob/master/logos/natgeowildhd.png?raw=true",National Geographic Wild
'''
novasport = '''#EXTINF:-1 tvg-id="Нова Спорт.bg" tvg-name="Nova Sport" tvg-logo="https://github.com/harrygg/EPG/blob/master/logos/novasport.png?raw=true",Nova Sport
'''
ringbg = '''#EXTINF:-1 tvg-id="RING.BG.bg" tvg-name="RING.BG" tvg-logo="https://github.com/harrygg/EPG/blob/master/logos/ringbg.png?raw=true",RING.BG
'''
dwnews = '''#EXTINF:-1 tvg-id="DW.bg" tvg-name="DW News" tvg-logo="https://yt3.googleusercontent.com/NSOdTQTWlqMy8O_j32dx-ftfTCHMOt04Hm7KZ4pfAK6-eQzQSZMWvvss90kG8KQfJ7iNP3phyA=s900-c-k-c0x00ffffff-no-rj",DW News
'''+dwnews_link+'''
'''
aljazeera = '''#EXTINF:-1 tvg-id="Al Jazeera.bg" tvg-name="Al Jazeera" tvg-logo="https://yt3.googleusercontent.com/IQJ3YwNpaJRPpOM1Gab8xBZiDhsgq2gtM3KZQKk8JCZjhxOPxuuzyUVCTWpyp9eAEyS-QQsdRA=s160-c-k-c0x00ffffff-no-rj",Al Jazeera
'''+aljazeera_link+'''
'''
agrotv = '''#EXTINF:-1 tvg-id="Agro TV" tvg-name="Agro TV" tvg-logo="http://logos.epg.cloudns.org/agrotv.png",Agro TV
'''+agrotv_link+'''
'''
tv1 = '''#EXTINF:-1 tvg-id="TV1.bg" tvg-name="TV1" tvg-logo="http://logos.epg.cloudns.org/tv1.png",TV1
'''+tv1_link+'''
'''
bnt2 = '''#EXTINF:-1 tvg-id="БНТ2.bg" tvg-name="БНТ 2" tvg-logo="http://logos.epg.cloudns.org/bnt2.png",БНТ 2
'''+bnt2_link+'''
'''
bnt3 = '''#EXTINF:-1 tvg-id="БНТ HD.bg" tvg-name="БНТ 3 HD" tvg-logo="http://logos.epg.cloudns.org/bnt3.png",БНТ 3 HD
'''+bnt3_link+'''
'''
bnt4 = '''#EXTINF:-1 tvg-id="БНТ Свят.bg" tvg-name="БНТ 4" tvg-logo="http://logos.epg.cloudns.org/bnt4.png",БНТ 4
'''+bnt4_link+'''
'''
sto_auto_moto = '''#EXTINF:-1 tvg-id="100% Auto Moto TV" tvg-name="100% Auto Moto TV" tvg-logo="http://epg.cloudns.org/tv/logos/automoto.png",100% Auto Moto TV
'''+sto_auto_moto_link+'''
'''
traveltv = '''#EXTINF:-1 tvg-id="Travel TV.bg" tvg-name="Travel TV" tvg-logo="http://logos.epg.cloudns.org/travel.png",Travel TV
'''+traveltv_link+'''
'''
thisisbg = '''#EXTINF:-1 tvg-id="This is Bulgaria" tvg-name="This is Bulgaria HD" tvg-logo="http://logos.epg.cloudns.org/thisisbg.png",This is Bulgaria HD
'''+thisisbg_link+'''
'''
thevoice = '''#EXTINF:-1 tvg-id="The Voice.bg" tvg-name="The Voice" tvg-logo="http://logos.epg.cloudns.org/thevoice.png",The Voice
'''+thevoice_link+'''
'''
citytv = '''#EXTINF:-1 tvg-id="City TV" tvg-name="City TV" tvg-logo="http://logos.epg.cloudns.org/city.png",City TV
'''+citytv_link+'''
'''
magictv = '''#EXTINF:-1 tvg-id="Magic TV" tvg-name="Magic TV" tvg-logo="http://logos.epg.cloudns.org/magictv.png",Magic TV
'''+magictv_link+'''
'''
darikradio = '''#EXTINF:-1 tvg-id="darik" tvg-name="Дарик Радио" tvg-logo="http://logos.epg.cloudns.org/darikradiotv.png",Дарик Радио
'''+darikradio_link+'''
'''
radiovitosha = '''#EXTINF:-1 tvg-id="vitosha" tvg-name="Радио Витоша" tvg-logo="https://www.radiovitosha.com/resources/assets/images/logo.svg",Радио Витоша
'''+radiovitosha_link+'''
'''




radiohorizont = '''#EXTINF:-1 tvg-id="horizont" tvg-name="Програма Хоризонт" tvg-logo="http://logos.epg.cloudns.org/bnrhorizont.png",Програма Хоризонт
'''+radiohorizont_link+'''
'''
radiohristobotev = '''#EXTINF:-1 tvg-id="hristo botev" tvg-name="Програма Христо Ботев" tvg-logo="http://logos.epg.cloudns.org/bnrhristobotev.png",Програма Христо Ботев
'''+radiohristobotev_link+'''
'''
radiosofia = '''#EXTINF:-1 tvg-id="radio sofia" tvg-name="Радио София" tvg-logo="https://yt3.googleusercontent.com/aPFZlAjocLAPL25arvUX5g3L2u-CWx441G3YYZ5eLZeAXe0d7X-GGtpcF0g-nNNslbX767JUEA=s900-c-k-c0x00ffffff-no-rj",Радио София
'''+radiosofia_link+'''
'''
radio1 = '''#EXTINF:-1 tvg-id="radio1" tvg-name="Радио 1" tvg-logo="http://epg.cloudns.org/tv/logos/radio1.png",Радио 1
'''+radio1_link+'''
'''
radio1rock = '''#EXTINF:-1 tvg-id="radio1 rock" tvg-name="Радио 1 Рок" tvg-logo="http://epg.cloudns.org/tv/logos/radio1rock.png",Радио 1 Рок
'''+radio1rock_link+'''
'''
radiozrock = '''#EXTINF:-1 tvg-id="z-rock" tvg-name="Радио Z-ROCK" tvg-logo="http://epg.cloudns.org/tv/logos/zrock.png",Радио Z-ROCK
'''+radiozrock_link+'''
'''
tangramegarock = '''#EXTINF:-1 tvg-id="tangramegarock" tvg-name="Tangra Mega Rock" tvg-logo="http://epg.cloudns.org/tv/logos/tangramegarock.png",Tangra Mega Rock
'''+tangramegarock_link+'''
'''
avtoradio = '''#EXTINF:-1 tvg-id="autoradio" tvg-name="Авторадио" tvg-logo="https://www.avtoradio.bg/ar_logo.f88b409f.png",Авторадио
'''+avtoradio_link+'''
'''
bgradio = '''#EXTINF:-1 tvg-id="bgradio" tvg-name="БГ Радио" tvg-logo="http://logos.epg.cloudns.org/bgradio.png",БГ Радио
'''+bgradio_link+'''
'''
btvradio = '''#EXTINF:-1 tvg-id="bTV Radio" tvg-name="bTV Радио" tvg-logo="http://logos.epg.cloudns.org/btv.png",bTV Радио
'''+btvradio_link+'''
'''
radionjoy = '''#EXTINF:-1 tvg-id="njoy" tvg-name="Радио N-JOY" tvg-logo="http://logos.epg.cloudns.org/njoy.png",Радио N-JOY
'''+radionjoy_link+'''
'''
radioenergy = '''#EXTINF:-1 tvg-id="NRG" tvg-name="Радио NRG" tvg-logo="http://logos.epg.cloudns.org/energy.png",Радио Energy
'''+radioenergy_link+'''
'''
radiofmplus = '''#EXTINF:-1 tvg-id="FM+" tvg-name="Радио FM+" tvg-logo="http://logos.epg.cloudns.org/fmplus.png",Радио FM+
'''+radiofmplus_link+'''
'''
radiofocus = '''#EXTINF:-1 tvg-id="Radio Focus" tvg-name="Радио Фокус" tvg-logo="https://www.sds.bg/wp-content/uploads/radio-focus.jpg",Радио Фокус
'''+radiofocus_link+'''
'''
radiofresh = '''#EXTINF:-1 tvg-id="Radio Fresh" tvg-name="Радио Fresh" tvg-logo="http://logos.epg.cloudns.org/radiofresh.png",Радио Fresh
'''+radiofresh_link+'''
'''



for elem in url_list:
    if "manifest" in elem:
        btv = btv+elem+'''
'''
    elif "ntv_2" in elem:
        nova = nova+elem+'''
'''
    elif "NNHD" in elem:
        nova_news = nova_news+elem+'''
'''
    elif "euronews" in elem:
        euronews = euronews+elem+'''
'''
    elif "bonair" in elem:
        bgonair = bgonair+elem+'''
'''
    elif "bloomberg" in elem:
        bloomberg = bloomberg+elem+'''
'''
    elif "btvcomedy" in elem:
        btvcomedy = btvcomedy+elem+'''
'''
    elif "btvaction" in elem:
        btvaction = btvaction+elem+'''
'''
    elif "btvcinema" in elem:
        btvcinema = btvcinema+elem+'''
'''
    elif "foxlife" in elem:
        starlife = starlife+elem+'''
'''
    elif "foxcrime" in elem:
        starcrime = starcrime+elem+'''
'''
    elif "kinonova" in elem:
        kinonova = kinonova+elem+'''
'''
    elif "axn" in elem:
        axn = axn+elem+'''
'''
    elif "viasatexplorer" in elem:
        viasatexplorer = viasatexplorer+elem+'''
'''
    elif "tlc" in elem:
        tlc = tlc+elem+'''
'''
    elif "discovery" in elem:
        discovery = discovery+elem+'''
'''
    elif ("natgeo" in elem and "natgeowild" not in elem):
        natgeo = natgeo+elem+'''
'''
    elif "natgeowild" in elem:
        natgeowild = natgeowild+elem+'''
'''
    elif "novasport" in elem:
        novasport = novasport+elem+'''
'''
    elif "ringbg" in elem:
        ringbg = ringbg+elem+'''
'''


m3u8_content = (
                extm3u+
                bnt1+btv+
                nova+
                nova_news+
                euronews+
                bgonair+
                bloomberg+
                btvcomedy+
                btvaction+
                btvcinema+
                starlife+
                starcrime+
                kinonova+
                axn+
                viasatexplorer+
                tlc+
                discovery+
                natgeo+
                natgeowild+
                novasport+
                ringbg+
                dwnews+
                aljazeera+
                agrotv+
                tv1+
                bnt2+
                bnt3+
                bnt4+
                sto_auto_moto+
                traveltv+
                thisisbg+
                thevoice+
                citytv+
                magictv+
                darikradio+
                radiovitosha+
                radiohorizont+
                radiohristobotev+
                radiosofia+
                radio1+
                radio1rock+
                radiozrock+
                tangramegarock+
                avtoradio+
                bgradio+
                btvradio+
                radionjoy+
                radioenergy+
                radiofmplus+
                radiofocus+
                radiofresh
                )

f = open(m3ufilepath, mode='w', encoding='utf-8')
f.seek(0,2)
f.write(str(m3u8_content))
f.close()
time.sleep(2)

r = requests.post(threadfin_server+'/api/', headers={'Content-type': 'application/json'}, json={"cmd": "update.m3u"})
if 'true' in str(r.content):
    print('\n\n\n------------------------------------\nThreadfin updated its M3U playlist.')
r = requests.post(threadfin_server+'/api/', headers={'Content-type': 'application/json'}, json={"cmd": "update.xmltv"})
if 'true' in str(r.content):
    print('Threadfin updated its XMLTV.')
r = requests.post(threadfin_server+'/api/', headers={'Content-type': 'application/json'}, json={"cmd": "update.xepg"})
if 'true' in str(r.content):
    print('Threadfin updated its XEPG.')
