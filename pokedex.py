import requests as rq

def search_pokemon(name):
    response = rq.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
    print(response.json())

#https://pokeapi.co/docs/v2#pokemon-section

if __name__ == "__main__":
    search_pokemon("charmander")