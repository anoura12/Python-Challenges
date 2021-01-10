import PySimpleGUI as sg
import json
import requests


def pokemonType(pokemon):
    """
        Return the type of pokemon.

        Parameters:
            pokemon(str): pokemon name.

        Returns:
            type_name(str): pokemon type

    """
    request = requests.get("https://pokeapi.co/api/v2/pokemon/{}/".format(pokemon)) #gets information on the pokemon from pokeapi.
    text = json.loads(request.text) #converts json text into python values (dictionary)
    element = text['types'][0] #retrieves 'types' key containing the type of pokemon
                                # since 'types' contains one element as a list, it can be retrieved like this.

    type_name = element['type']['name'] #the element extracted is a dictionary. Hence, the type key is used to get 'name' which contains the type of pokemon.
    return(type_name)

def urlType(pokemon):
    """
        Return the url of type of pokemon.

        Parameters:
            pokemon(str): pokemon name.

        Returns:
            type_url(str): url of pokemon type.

    """
    request = requests.get("https://pokeapi.co/api/v2/pokemon/{}/".format(pokemon)) #gets information on the pokemon from pokeapi.
    text = json.loads(request.text) #converts json text into python values (dictionary)
    element = text['types'][0] #retrieves 'types' key containing the type of pokemon
                                # since 'types' contains one element as a list, it can be retrieved like this.

    type_url = element['type']['url'] #the element extracted is a dictionary. 
                                        #Hence, the type key is used to get 'url' which has the url of the pokemon type.
    return(type_url)

def doubledamageFrom(url):
    """
        Return a list of types that give double damage to the pokemon.

        Parameters:
            url(str): url of the type of pokemon.

        Returns:
            ddamage(list): list of types that cause double damage.

    """
    request = requests.get(url) #gets information on Pokemon from pokeapi.
    text = json.loads(request.text) #converts json text into python values (dictionary)
    ddamage = []
    
    element = text['damage_relations']['double_damage_from'] #retrieve double_damage list
    number_of_types = len(element)
    for x in range(number_of_types):#loop for extracting each type causing double damage.
         double_damage = element[x]['name'] 
         ddamage.append(double_damage)

    return(ddamage)

def halfdamageFrom(url):
    """
        Return the list of types of pokemon that cause half damage.

        Parameters:
            url(str): url of the type of pokemon.

        Returns:
            hdamage(list): list of types of pokemon that cause half damage.

    """
    request = requests.get(url) #gets information on Pokemon from pokeapi.
    text = json.loads(request.text) #converts json text into python values (dictionary)
    hdamage = []
    
    element = text['damage_relations']['half_damage_from'] #retrieve double_damage list
    number_of_types = len(element)
    for x in range(number_of_types):#loop for extracting types that cause half damage.
         half_damage = element[x]['name'] 
         hdamage.append(half_damage)

    return(hdamage)

def doubledamageUrl(url):
    """
        Return the list of the urls of the types that cause double damage.

        Parameters:
            url(str): url for the type of pokemon.

        Returns:
            urldamage(list): list of urls of types that cause double damage.

    """
    request = requests.get(url) #gets information on Pokemon from pokeapi.
    text = json.loads(request.text) #converts json text into python values (dictionary)
    urldamage = []
    
    element = text['damage_relations']['double_damage_from'] #retrieve double_damage list
    number_of_types = len(element)
    for x in range(number_of_types):# loop for extracting the url of types causing double damage.
         double_damage = element[x]['url'] 
         urldamage.append(double_damage)

    return(urldamage)


def fivePokemon(damageUrl):
    """
        Return the list of five pokemon from each type causing double damage.

        Parameters:
            damageUrl(list):list of urls of the types that cause double damage.

        Returns:
            pokem(list): list of five pokemon of each type that causes double damage.

    """
    request = requests.get(damageUrl) #gets information on Pokemon from pokeapi.
    text = json.loads(request.text) #converts json text into python values (dictionary)
    pokem = []

    for i in range(5): #loop for extracting 5 pokemon
        element = text['pokemon'][i]['pokemon']
        name = element['name']
        pokem.append(name)

    return(pokem)


def ability(pokemon):
    """
        Return the list of the abilities that the pokemon has.

        Parameters:
            pokemon(str): pokemon name.

        Returns:
            set_of_abilities(list): list of abilities that the pokemon has.

    """
    pokemon = pokemon.lower()#converts pokemon name into lowercase.
    request = requests.get("https://pokeapi.co/api/v2/pokemon/{}/".format(pokemon)) #gets info on pokemon from the pokeapi.
    text = json.loads(request.text)
    abilities = text['abilities']
    number_of_abilities = len(abilities)
    set_of_abilities = []

    for count in range(number_of_abilities): #loop that extracts each kind of ability.
        element = abilities[count]
        ability = element['ability']
        name = ability['name']
        set_of_abilities.append(name)

    return(set_of_abilities)

#creates inquiry window
layout = [[sg.Text("Which Pokemon would you like to find more info about?")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Window Title', layout)


while True:
    event, values = window.read() #displays the inquiry window.
    
    if event == sg.WINDOW_CLOSED or event == 'Quit': #condition to exit from window.
        break

    if(event == 'Ok'): #condition to open window with pokemon info.
        input_value = values['-INPUT-'].lower()

        #calling all functions.
        poketype = pokemonType(input_value)
        urltype = urlType(input_value)
        doubleDamage = doubledamageFrom(urltype)
        halfDamage = halfdamageFrom(urltype)
        ddURL = doubledamageUrl(urltype)
        length = len(ddURL)
        dictionary = {}
        ff = []
        for x in range(length):#loop to create a list that contains the five pokemon according to type.
            fp = fivePokemon(ddURL[x])
            ff.append(fp)
        
        for y in range(length): #loop to create a dictionary to assign 'damage type' to a key and 'five pokemon' to that key.
            key = doubleDamage[y]
            value = ff[y]
            dictionary.setdefault(key,value)

        pokemon_abilities = ability(input_value)        

    #creates window displaying pokemon info.
    layout2 = [[sg.Text("The Pokemon is " + values['-INPUT-'])],
             [sg.Text("It's type is " + poketype)],
             [sg.Text("It recieves double damage from - " + str(doubleDamage))],
             [sg.Text("It recieves half damage from - " + str(halfDamage))]]
             [sg.Text("Five pokemon according to their type are - " + str(dictionary))],
             [sg.Text("Pokemon abilities - " + str(pokemon_abilities))],
             [sg.Button("Done")]]

    win = sg.Window('Pokemon' , layout2)
    e,v = win.read()#displays the window with pokemon info 

    win.close()

window.close()



