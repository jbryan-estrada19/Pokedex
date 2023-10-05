import streamlit as st
import functions as fn
import pokedex as dex



pokebelt = fn.get_pokemon()

def add_pokemon():
    pokemon = st.session_state['new_pokemon'] + "\n"
    pokebelt.append(pokemon)
    print(pokemon)
    fn.write_pokemon(pokebelt)

# def add_item():
#     item = st.session_state['new_item'] + "\n"
    

st.title("My Pokemon Team")
st.text_input(label = "Add new pokemon", placeholder="Who's that Pokemon?", 
              on_change=add_pokemon, key='new_pokemon')

stripped_pokebelt = []
for i in pokebelt:
    stripped_pokebelt.append(i.strip())

for pokemon in stripped_pokebelt:
    col1, col2 = st.columns(2)    

    with col1:
        #-------------------------------------------------------------------------------------
        #implement an if try function
        st.subheader(pokemon.capitalize())
        #----------------------------------------------------------------------------------------
        #Run only when pokemon is not found in the csv
        pokemon_details = dex.search_pokemon(pokemon)
        image = f"https://unpkg.com/pokeapi-sprites@2.0.2/sprites/pokemon/other/dream-world/{pokemon_details[0]}.svg"
        st.image(image, width = 200 )
        # st.text_input(label = "Held item", placeholder="Which item?", 
        #       on_change=add_item, key='new_item')
        
#-------------------------------------------------------------
#add a delete pokemon function
# for index,todo in enumerate(todos):
#     col1, col2 = st.columns([2, 8])
#     with col2: 
#         st.markdown(todo)
#     with col1:
#         delete = st.button(f":wastebasket: {index+1}.)", key= todo) # 
#     if delete:
#         todos.pop(index)
#         functions.write_todos(todos)
#         del st.session_state[todo]
#         st.rerun()




    with col2:
        #-----------------------------------------------------------------------------------------
        #Store to csv as a dict, then retrieve
        st.write(f"""\n
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
