from hywrap import duels
import asyncio

key = "INSERT API KEY HERE"

skywarsStats = asyncio.get_event_loop().run_until_complete(duels("568e9c0662504e8695a809bb277baa9b", key))
print(skywarsStats)