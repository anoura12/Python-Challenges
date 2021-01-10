import json
import requests

def ability(pokemon):
    pokemon = pokemon.lower() #converts pokemon name to lowercase
    request = requests.get("https://pokeapi.co/api/v2/pokemon/{}/".format(pokemon)) #extracts pokemon from pokeapi
    text = json.loads(request.text)
    abilities = text['abilities'] #extracts abilities
    number_of_abilities = len(abilities) #extracts number of abilities
    set_of_abilities = [] #list to store all abilities

    for count in range(number_of_abilities):#loop through the number of abilities and extract each one.
        element = abilities[count]
        ability = element['ability']
        name = ability['name']
        set_of_abilities.append(name)

    return(set_of_abilities)

