import requests

def bedwars(uuid : str, hypixelapikey : str = None):
    if hypixelapikey is None:
        print("Please Enter a Hypixel API Key!")
    else:
        api = requests.get(f"https://api.hypixel.net/player?key={hypixelapikey}&uuid={uuid}").json()
        return api["player"]["stats"]["Bedwars"]

def skywars(uuid : str, hypixelapikey : str = None):
    if hypixelapikey is None:
        print("Please Enter a Hypixel API Key!")
    else:
        api = requests.get(f"https://api.hypixel.net/player?key={hypixelapikey}&uuid={uuid}").json()
        return api["player"]["stats"]["SkyWars"]

def duels(uuid : str, hypixelapikey : str = None):
    if hypixelapikey is None:
        print("Please Enter a Hypixel API Key!")
    else:
        api = requests.get(f"https://api.hypixel.net/player?key={hypixelapikey}&uuid={uuid}").json()
        return api["player"]["stats"]["Duels"]

def arcade(uuid : str, hypixelapikey : str = None):
    if hypixelapikey is None:
        print("Please Enter a Hypixel API Key!")
    else:
        api = requests.get(f"https://api.hypixel.net/player?key={hypixelapikey}&uuid={uuid}").json()
        return api["player"]["stats"]["Arcade"]

def buildBattle(uuid : str, hypixelapikey : str = None):
    if hypixelapikey is None:
        print("Please Enter a Hypixel API Key!")
    else:
        api = requests.get(f"https://api.hypixel.net/player?key={hypixelapikey}&uuid={uuid}").json()
        return api["player"]["stats"]["BuildBattle"]

def pit(uuid : str, hypixelapikey : str = None):
    if hypixelapikey is None:
        print("Please Enter a Hypixel API Key!")
    else:
        api = requests.get(f"https://api.hypixel.net/player?key={hypixelapikey}&uuid={uuid}").json()
        return api["player"]["stats"]["Pit"]

def skyblock(uuid : str, hypixelapikey : str = None):
    if hypixelapikey is None:
        print("Please Enter a Hypixel API Key!")
    else:
        api = requests.get(f"https://api.hypixel.net/player?key={hypixelapikey}&uuid={uuid}").json()
        return api["player"]["stats"]["SkyBlock"]