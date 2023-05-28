import requests

pokemon_ids = [1, 2, 3, 4, 5, 6]

for pokemon_id in pokemon_ids:
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_id)
    response = requests.get(url)
    pokemon = response.json()
    with open('pokemon.txt', 'r') as pokemon_file:
        add = pokemon_file.read()
        add = add + format(pokemon['id']) + ' ' + format(pokemon['name']) + ' \n'
        moves = pokemon['moves']
        for move in moves:
            add = add + format((move['move']['name'])) + ' \n'
            with open('pokemon.txt', 'w+') as pokemon_file:
                pokemon_file.write(add)
