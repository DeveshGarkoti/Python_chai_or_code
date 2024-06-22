# List Uniqeness checker
# Problem: check is all the element in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

items = ["apple","banana","orange","Mango","apple","lichi"]


# for i in items:
#   if items.count(i) > 1:
#     print(f"Duplicate found: {i}")
#     break

unique_item = set()

for item in items:
  if item in unique_item:
    print("Duplicate: ", item)
    break
  unique_item.add(item)
