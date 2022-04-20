import requests


def get_poke_info(poke_name): 
    """
    queries the poke API for information related to the pokemon specified 
    
    :param name: Pokemon's name or Pokedex number
    """
    print("Retrieving Pokemon information...", end='')
    URL = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(URL + poke_name)

    if response.status_code == 200:
        print("Success")
        return response.json()

    else:
        print('failed. Response code:', response.status_code)
        return