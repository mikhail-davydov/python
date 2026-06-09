import json
from zipfile import ZipFile

def load_json(s):
    try:
        return json.loads(s)
    except:
        return None

players = []

with ZipFile('data.zip') as zip_file:
    for file in zip_file.infolist():
        player = load_json(zip_file.read(file))
        if player and player['team'] == 'Arsenal':
            players.append(f'{player["first_name"]} {player["last_name"]}')

for name in sorted(players):
    print(name)
