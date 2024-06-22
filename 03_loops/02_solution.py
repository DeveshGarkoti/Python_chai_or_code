# Sum of even numbers

number = 100
sum_of_even_number = 0

for num in range(1, number+1):
  if num % 2 == 0:
    sum_of_even_number += num
  
print(sum_of_even_number)