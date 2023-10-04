import requests as rq
import streamlit as st

@st.cache_data


def search_pokemon(name):
    response = rq.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
    if response.status_code == 200:
        try:
            response.raise_for_status()  # Raise an exception for HTTP errors
            searched_pokemon = response.json()
            poke_name = searched_pokemon["name"]
            poke_id = searched_pokemon["id"]
            base_stat = searched_pokemon["stats"]
            base_hp = base_stat[0]["base_stat"]
            base_atk = base_stat[1]["base_stat"]
            base_def = base_stat[2]["base_stat"]
            base_satk = base_stat[3]["base_stat"]
            base_sdef = base_stat[4]["base_stat"]
            base_spd = base_stat[5]["base_stat"]
            poke_stats = [poke_id, poke_name, base_hp, base_atk, base_def, base_satk, base_sdef, base_spd]
            return poke_stats
        except rq.exceptions.HTTPError as e:
            print(f"Error: {e}")
            return None  # Return None if the Pokemon is not found or there's an HTTP error
        except rq.exceptions.RequestException as e:
            print(f"Request Exception: {e}")
            return None  # Handle other request exceptions gracefully
        except ValueError as e:
            print(f"JSON Decode Error: {e}")
            return None  # Handle JSON decode errors gracefully








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