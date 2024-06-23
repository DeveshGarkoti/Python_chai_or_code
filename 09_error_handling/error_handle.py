file = open('youtube.txt', 'w')

try:
  file.write("Chai or Code")
finally:
  file.close()

with open('youtube.txt','w') as file:
  file.write("Chai or python")