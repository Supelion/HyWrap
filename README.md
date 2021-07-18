<h1>HyWrap</h1>

Another one of those Hypixel API Wrappers.
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
<br/>
<br/>
<br/>
<br/>

- `hywrap.bedwars(uuid, key)` - Displays a given user's Bedwars Stats
- `hywrap.skywars(uuid, key)` - Display's a given user's Skywars Stats
- `hywrap.duels(uuid, key)` - Display's a given user's Duels Stats.
- `hywrap.arcade(uuid, key)` - Display's a given user's Arcade Stats.
- `hywrap.duels(uuid, key)` - Display's a given user's Duels Stats.
- `hywrap.buildBattle(uuid, key)` - Display's a given user's Build Battle Stats.
- `hywrap.pit(uuid, key)` - Display's a given user's Pit Stats.
- `hywrap.skyblock(uuid, key)` - Display's a given user's SkyBlock Stats.
