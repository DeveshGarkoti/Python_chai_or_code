# Timing Function Execution
# Write a decorator that measures the time a function takes to execute

# # Decorator
# def timer(func):
#   def wrapper(*args, **kwargs):
#     result = func(*args, **kwargs)
#     return result
#   return wrapper

import time

def timer(func):
  def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"{func.__name__} ran in {end - start} time")
    return result
  return wrapper


@timer
def example_function(n):
  time.sleep(n)


example_function(2)