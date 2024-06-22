distace = 5

if distace < 3:
  transport = "walk"
elif distace <= 15:
  transport = "Bike"
else:
  transport = "Car"

print(transport)