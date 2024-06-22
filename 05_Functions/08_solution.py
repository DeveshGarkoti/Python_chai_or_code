# Function with **kwargs

def print_kwargs(**kwargs):
  for key, value in kwargs.items():
    print(f"{key} = {value}")

print_kwargs(name="Devesh", power="super human")
print_kwargs(name="Devesh")
