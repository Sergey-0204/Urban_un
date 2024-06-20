#water = ["coca", "fanta", "pepsi"]
#print(water)
#print(water[2])
#water[1] = "vodka"
#print(water)


water = ["coca", "fanta", "pepsi"]
water.append(True)
print(water)
water.extend(["string",2])
print(water)
print("coca" not in water)
print(water[0:2:2])
