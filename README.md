
<h1>HyWrap</h1>

An Asynchronous Hypixel API Wrapper
<br/>
<br/>
<br/>

**Basic Example:**
<br/>

*Bedwars:*
```py
from hywrap import bedwars
import asyncio

key = "INSERT API KEY HERE"

bedwarsStats = asyncio.get_event_loop().run_until_complete(bedwars("568e9c0662504e8695a809bb277baa9b", key))
print(bedwarsStats)
```
<br/>

*Skywars:*
```py
from hywrap import skywars
import asyncio

key = "INSERT API KEY HERE"

skywarsStats = asyncio.get_event_loop().run_until_complete(skywars("568e9c0662504e8695a809bb277baa9b", key))
print(skywarsStats)
```
<br/>
<br/>

**NOTE:** Because of an issue with Python, you cannot simply do `asyncio.run(hywrap.{gamemode})` on windows.

<br/>
<br/>

- `hywrap.player(uuid, key)` - Displays the entire API page for a user.
- `hywrap.bedwars(uuid, key)` - Displays a given user's Bedwars Stats
- `hywrap.skywars(uuid, key)` - Display's a given user's Skywars Stats
- `hywrap.duels(uuid, key)` - Display's a given user's Duels Stats.
- `hywrap.arcade(uuid, key)` - Display's a given user's Arcade Stats.
- `hywrap.duels(uuid, key)` - Display's a given user's Duels Stats.
- `hywrap.buildBattle(uuid, key)` - Display's a given user's Build Battle Stats.
- `hywrap.pit(uuid, key)` - Display's a given user's Pit Stats.
- `hywrap.skyblock(uuid, key)` - Display's a given user's SkyBlock Stats.
- `hywrap.boosters(key)` - Displays the active boosters on the network.
- `hywrap.status(uuid, key)` - Returns a given player's status.
- `hywrap.rankedSkywars(uuid, key)` - Returns the ranked skywars API endpoint.
- `hywrap.playerCount(key)` - Displays the active player count on the network including counts for seperate gamemodes.
- `hywrap.leaderboards(key)` - Displays the leaderboards.
- `hywrap.watchdogStats(key)` - Displays the WatchDog Statistics.
- `hywrap.guild(uuid, key)`- Returns the entire Hypixel Guild API Page for a given user.
- `hywrap.recentGames(uuid, key)` - Returns the recent games of a player.
- `hywrap.friends(uuid, key)` - Returns the friends API endpoint of a player.
- `hywrap.key(key)` - Returns the provided API key's information.
- `hywrap.checkUUID(username)` - Returns the UUID of a provided player's name.
