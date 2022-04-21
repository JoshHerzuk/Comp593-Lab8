import requests


def get_poke_info(name): 
    """
    queries the poke API for information related to the pokemon specified 
    
    :param name: Pokemon's name or Pokedex number
    """
    print("Retrieving Pokemon information...", end='')
    

    if name is None:
        return

    name = name.lower().strip()

    if name == '':
        return
        
    URL = 'https://pokeapi.co/api/v2/pokemon/' + str(name)
   
    response = requests.get(URL)

    if response.status_code == 200:
        print("Success")
        return response.json()

    else:
        print('failed. Response code:', response.status_code)
        return