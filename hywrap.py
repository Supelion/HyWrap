import aiohttp

async def bedwars(uuid : str, hypixelapikey : str = None):
    if hypixelapikey is None:
        print("Please Enter a Hypixel API Key!")
    if uuid is None:
        print("Please specify a UUID!")
    else:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.hypixel.net/player?key={hypixelapikey}&uuid={uuid}') as bedwarsRaw:
                rawBW = await bedwarsRaw.json()
                bedwarsStats = rawBW["player"]["stats"]["Bedwars"]
                return bedwarsStats

async def skywars(uuid : str, hypixelapikey : str = None):
    if hypixelapikey is None:
        print("Please Enter a Hypixel API Key!")
    if uuid is None:
        print("Please specify a UUID!")
    else:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.hypixel.net/player?key={hypixelapikey}&uuid={uuid}') as skywarsRaw:
                rawSW = await skywarsRaw.json()
                skywarsStats = rawSW["player"]["stats"]["SkyWars"]
                return skywarsStats

async def duels(uuid : str, hypixelapikey : str = None):
    if hypixelapikey is None:
        print("Please Enter a Hypixel API Key!")
    if uuid is None:
        print("Please specify a UUID!")
    else:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.hypixel.net/player?key={hypixelapikey}&uuid={uuid}') as duelsRaw:
                rawDuels = await duelsRaw.json()
                duelsStats = rawDuels["player"]["stats"]["Duels"]
                return duelsStats

async def arcade(uuid : str, hypixelapikey : str = None):
    if hypixelapikey is None:
        print("Please Enter a Hypixel API Key!")
    if uuid is None:
        print("Please specify a UUID!")
    else:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.hypixel.net/player?key={hypixelapikey}&uuid={uuid}') as arcadeRaw:
                rawArcade = await arcadeRaw.json()
                arcadeStats = rawArcade["player"]["stats"]["Arcade"]
                return arcadeStats


async def buildBattle(uuid : str, hypixelapikey : str = None):
    if hypixelapikey is None:
        print("Please Enter a Hypixel API Key!")
    if uuid is None:
        print("Please specify a UUID!")
    else:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.hypixel.net/player?key={hypixelapikey}&uuid={uuid}') as buildRaw:
                rawBuild = await buildRaw.json()
                buildBattleStats = rawBuild["player"]["stats"]["BuildBattle"]
                return buildBattleStats

async def pit(uuid : str, hypixelapikey : str = None):
    if hypixelapikey is None:
        print("Please Enter a Hypixel API Key!")
    if uuid is None:
        print("Please specify a UUID!")
    else:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.hypixel.net/player?key={hypixelapikey}&uuid={uuid}') as pitRaw:
                rawPit = await pitRaw.json()
                pitStats = rawPit["player"]["stats"]["Pit"]
                return pitStats

async def skyblock(uuid : str, hypixelapikey : str = None):
    if hypixelapikey is None:
        print("Please Enter a Hypixel API Key!")
    if uuid is None:
        print("Please specify a UUID!")
    else:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.hypixel.net/player?key={hypixelapikey}&uuid={uuid}') as sbraw:
                rawSB = await sbraw.json()
                skyblockStats = rawSB["player"]["stats"]["SkyBlock"]
                return skyblockStats
