import json 

with open('film.json', 'rb') as r:
    data_film = json.load(r)

data_list = []

for films in data_film:
    if data_film[films]['ID'] not in  data_list:
        data_list.append(data_film[films]['ID'])
    else:
        print(data_film[films]['ID'])

print(len(data_list))
