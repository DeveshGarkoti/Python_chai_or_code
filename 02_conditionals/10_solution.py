# Pet Food Recomandation

pet_species = "Dog"
pet_age = 2

if pet_species == "Dog":
  if pet_age < 2:
    pet_food = "Puppy Food"
  else:
    pet_food = "Adult Dog Food"
elif pet_species == "Cat":
  if pet_age < 5:
    pet_food = "Kitten Food"
  else:
    pet_food = "Senior Cat Food"

print(" Food for your pet is", pet_food)