# Debugging Function Calls
def debug(func):
  def wrapper(*args, **kwargs):
    args_value = ', '.join(str(arg) for arg in args)
    kwargs_value = ', '.join(f"{k} = {v}" for k,v in kwargs.items())
    print(f"calling: {func.__name__} with \n args {args_value} and \n kwargs {kwargs_value}")

    result = func(*args, **kwargs)
    return result
  return wrapper


@debug
def greet(name, greeting = "Hello"):
  print(f"{greeting} {name}")

greet("Devesh",greeting="kese ho")