username = "Devesh"

def func():
  username = "chai"
  print("Inside function: ", username)


x = 99

def f1():
  x = 88
  def f2():
    print(x)
  return f2

myResult = f1()
myResult()

def chaiCoder(num):
  def actual(x):
    return x ** num
  return actual


square = chaiCoder(2)
cube = chaiCoder(3)

print(square(3))
print(cube(3))