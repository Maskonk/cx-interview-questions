import json
import math

with open('Offers.json', 'r') as f:
    offers = json.load(f)

print(offers["get1free"]["Baked Beans"]["qualifying amount"])

print(math.floor(5 / 2))
