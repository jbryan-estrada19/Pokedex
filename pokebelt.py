import streamlit as st
import functions as fn
import pokedex as dex

pokebelt = fn.get_pokemon()

def add_pokemon():
    pokemon = st.session_state['add_pokemon'] + "\n"
    pokebelt.append(pokemon)
    print(pokemon)
    fn.write_pokemon(pokebelt)




for pokemon in pokebelt:
    st.subheader(pokemon)
    st.write(dex.search_pokemon(pokemon))
    #st.columns() #Choose possible/learnable attacks
    #st.write() #Held item 

st.title("My Pokemon Team")

st.text_input(label = "Add new pokemon", placeholder="Who's that Pokemon?", 
              on_change=add_pokemon, key='new_pokemon')

