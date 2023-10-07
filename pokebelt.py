import streamlit as st
import functions as fn

pokebelt = fn.get_pokemon()

def add_pokemon():
    pokemon = st.session_state['new_pokemon'] + "\n"
    pokebelt.append(pokemon.lower())
    #print(pokemon)
    fn.write_pokemon(pokebelt)

st.title("My Pokemon Team")
st.text_input(label = "Add new pokemon", placeholder="Who's that Pokemon?", 
              on_change=add_pokemon, key='new_pokemon')

stripped_pokebelt = []
for i in pokebelt:
    stripped_pokebelt.append(i.strip())

for pokemon in stripped_pokebelt:
    pokemon_details = fn.read_file(pokemon)[0]
    