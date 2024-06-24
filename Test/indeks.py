#water = ["coca", "fanta", "pepsi"]
#print(water)
#print(water[2])
#water[1] = "vodka"
#print(water)
from typing import List

water: list[str | bool | int] = ["coca", "fanta", "pepsi", True]
print(water)
water.extend(["string", 2])
print(water)
print("coca" not in water)
print(water[0:2:2])
