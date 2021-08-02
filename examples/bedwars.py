from hywrap import bedwars
import asyncio

key = "INSERT API KEY HERE"

bedwarsStats = asyncio.get_event_loop().run_until_complete(bedwars("568e9c0662504e8695a809bb277baa9b", key))
print(bedwarsStats)