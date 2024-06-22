# Function Returning Multiple values
# Problem: Create a function that returns both area and circumference of a circle given its radius.

# Solution
import math

def circle(radius):
  area_of_circle = math.floor(math.pi * radius**2) 
  circumfrence_of_circle = math.floor(2 * math.pi * radius)
  return area_of_circle, circumfrence_of_circle


a , c = circle(7)
 
print("Area: ", a, ", Circumference: ",c)