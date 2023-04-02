from api import app
import json
import os
from auth.auth import *
from pathlib import Path

path = os.path.join(Path(__file__).parent, 'auth')

if not os.path.exists(path):
    os.mkdir('auth')

if not os.path.exists(f'{path}/keys.json'):
    with open('auth/keys.json', 'w') as file:
        json.dump([], file, indent=4)

with open(f'{path}/keys.json', 'r') as file:
    data = json.load(file)

if data == []:
    key = generate_key()
    
while True:
    inp = input('$ ')
    if inp == 'key':
        print(data)
    elif inp == "exit":
        break
    elif 'start' in inp:
        lis = inp.split(' ')
        host = lis[1]
        port = lis[2]
        app.run(debug = True, host = host, port = port)
