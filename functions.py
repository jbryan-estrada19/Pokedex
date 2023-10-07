import functions as fn
import requests as rq
import pandas as pd
import csv
import streamlit as st
#Gets the list of entered pokemon from pokebelt.txt
def get_pokemon(filepath="pokebelt.txt"):
    with open(filepath, 'r') as file:
        pokemon_store = file.readlines()  # puts the file's contents to todos
    return pokemon_store

#Writes entries to pokebelt.txt
def write_pokemon(poke_arg, filepath="pokebelt.txt"):
    with open(filepath, 'w') as file:
        file.writelines(poke_arg)
    return

#Writes data to pokemon.csv
def write_file(entry, filepath='pokemon.csv'):
    with open(filepath, mode='a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(entry)
        print(f'Pokemon added to {filepath}')

#Get pokemon data from PokeAPI
def search_pokemon(entry):
    response = rq.get(f"https://pokeapi.co/api/v2/pokemon/{entry}/")
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
        except KeyError as e:
            print("No problems I don't think?")

#Decision making: pokemon in csv? 
def read_file(pokemon, filepath='pokemon.csv'):
    df = pd.read_csv(filepath)
    result = df.query(f"poke_name=='{pokemon}'")
    if not result.empty:
        pokemon_details = fetch_pokemoncsv(result)
        create_column(pokemon_details)
    else:
        pokemon_details = add_pokemonapi(pokemon)
        create_column(pokemon_details)
    return pokemon_details

#Fetches pokemon details from pokemon.csv
def fetch_pokemoncsv(result):
    pokemon_details = result.values.tolist()[0]
    return pokemon_details

#Fetches pokemon details from pokeAPI.com
def add_pokemonapi(pokemon):
    print(f'No {pokemon} Pokemon found in files. Searching the internet... ')
    pokemon_details = fn.search_pokemon(pokemon)
    fn.write_file(pokemon_details)
    return pokemon_details

#Creates column
def create_column(pokemon_details):
    col1, col2 = st.columns(2)    
    with col1:
        st.subheader(f"{pokemon_details[1].capitalize()}")
        image = f"https://unpkg.com/pokeapi-sprites@2.0.2/sprites/pokemon/other/dream-world/{str(pokemon_details[0])}.svg"
        st.image(image, width=200)
    with col2:
        st.write(f"""
                
                Pokemon: {pokemon_details[1]} \n
                ID: {pokemon_details[0]} \n
                Base HP: {pokemon_details[2]} \n
                Base Attack: {pokemon_details[3]} \n
                Base Defense: {pokemon_details[4]} \n
                Base Special Attack: {pokemon_details[5]} \n
                Base Special Defense: {pokemon_details[6]} \n
                Base Speed: {pokemon_details[7]}\n
                \n ________________
        
                """)
