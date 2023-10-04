def get_pokemon(filepath="pokebelt.txt"):
    with open(filepath, 'r') as file:
        pokemon_store = file.readlines()  # puts the file's contents to todos
    return pokemon_store


def write_pokemon(poke_arg, filepath="pokebelt.txt"):
    with open(filepath, 'w') as file:
        file.writelines(poke_arg)
    return

