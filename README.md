<h1>HyWrap</h1>

Another one of those Hypixel API Wrappers.
<br/>
<br/>
<br/>

**Basic Example:**
<br/>

*Bedwars:*
```py
import hywrap

key = "API KEY HERE"

print(hywrap.bedwars("568e9c0662504e8695a809bb277baa9b", key))
```

*Skywars:*
```py
import  hywrap

key = "API KEY HERE"

print(hywrap.skywars("568e9c0662504e8695a809bb277baa9b", key))
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
