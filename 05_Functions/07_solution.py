# Functions with *args

def sum_all(*args):
  print(*args)
  print(args)
  for i in args:
    print(i*2)
  return sum(args)

print(sum_all(1,2,2))
# print(sum_all(1,2,2,5,6,7))