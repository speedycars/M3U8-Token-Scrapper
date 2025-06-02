import requests
import configparser
import ast
import pathlib
import requests

config_path = pathlib.Path(__file__).parent.absolute() / "config" / "config.cfg"
config = configparser.ConfigParser()
config.read(config_path, encoding='utf-8')

threadfin_server = ast.literal_eval(config.get('CONFIG', 'threadfin_server'))
plexpublichostname = ast.literal_eval(config.get('CONFIG', 'plexpublichostname'))
plextoken = str(config.get('CONFIG', 'plextoken'))

r = requests.post(threadfin_server+'/api/', headers={'Content-type': 'application/json'}, json={"cmd": "update.m3u"})
if 'true' in str(r.content):
    print('Threadfin updated its M3U playlist.')
r = requests.post(threadfin_server+'/api/', headers={'Content-type': 'application/json'}, json={"cmd": "update.xmltv"})
if 'true' in str(r.content):
    print('Threadfin updated its XMLTV.')
r = requests.post(threadfin_server+'/api/', headers={'Content-type': 'application/json'}, json={"cmd": "update.xepg"})
if 'true' in str(r.content):
    print('Threadfin updated its XEPG.')
r = requests.post(plexpublichostname+'/livetv/dvrs/38/reloadGuide?X-Plex-Token='+plextoken)
print('Plex got signaled to update its EPG.')