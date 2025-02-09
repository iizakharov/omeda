import requests
import os

proxy  = ""


proxies = {
  "http"  : proxy,
  "https" : proxy,
}

# r = requests.get(url, headers=headers, proxies=proxies)
url = 'https://omeda.city/'
user = 'Mamut_rahal'
search_params = 'search?sq='
player_id = 'b7e290d1-7224-4fdc-87d3-4f39cb0a7842'
# res = requests.get(url + search_params + user, proxies=proxies)
player_stat = requests.get(f'{url}players/{player_id}.json', proxies=proxies).json()
page = 1
player_matches = {player_id : []}
while True:
    response = requests.get(f'{url}players/{player_id}/matches.json?time_frame=ALL&page={page}&per_page=100', proxies=proxies)
    if response.status_code != 200:
        break
    res = response.json()
    if not res['matches']:
        break
    matches = res['matches']
    for match in matches:
        match_id = match['id']
        date = match['end_time']
        mode = match['game_mode']
        if mode != 'ranked':
            continue
        winning_team = match['winning_team']
        for player in  match['players']:
            if player['id'] == player_id:
                player_team = player['team']
                minions_killed = player['minions_killed']
                kills = player['kills']
                role = player['role']
                deaths = player['deaths']
                assists = player['assists']
                vp = player['vp']
                rank = player['rank']
                vp_total = player['vp_total']
                vp_change = player['vp_change']
                rank_new = vp_total + vp_change if vp_total else vp_change
                break
        player_matches[player_id].append([match_id, date, mode, winning_team, player_team, role, minions_killed,
                                          kills, deaths, assists, vp, rank, vp_total, vp_change, rank_new])
    page += 1

print()
