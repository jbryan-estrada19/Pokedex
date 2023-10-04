import requests as rq


def search_pokemon(name):
    response = rq.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
    pokemon = response.json()
    poke_name = pokemon["name"]
    poke_id = pokemon["id"]
    base_stat = pokemon["stats"]
    base_hp = (base_stat[0])['base_stat']
    base_atk =(base_stat[1])['base_stat']
    base_def = (base_stat[2])['base_stat']
    base_satk = (base_stat[3])['base_stat']
    base_sdef = (base_stat[4])['base_stat']
    base_spd = (base_stat[5])['base_stat']
    poke_stats = [poke_id,poke_name,base_hp,base_atk,base_def,base_satk,base_sdef,base_spd]
    return poke_stats


    

#https://pokeapi.co/docs/v2#pokemon-section



#input: python pokedex.py <name of pokemon>

#output: 
# Name: Pikachu
# ID: 25
# Base XP: 112
# Base HP: 35
# Base Attack: 55
# Base Defense: 40
# Base Special Attack: 50
# Base Special Defense: 50
# Base Speed: 90