import time
from functools import wraps # preseves the original function metadata

def monitor(retries=3):  # outer function
  def decorator(func):   # recives your function
    @wraps(func)         # Preseves the original function metadate
    def wrapper(*args, **kwargs): ## actually runs when you call it
      attempt = 0

      while attempt < retries:
        try: 
          print(f"[LOG] Calling a Function: {func.__name__}")
          start = time.time()

          results = func(*args, **kwargs)

          end = time.time()
          print(f"[LOG] Execution time: {end - start:.4f} seconds")

          print(f"[LOG] Function {func.__name__} completed successfully\n")

          return results

        except Exception as e:
          attempt += 1
          print(f"[ERROR] attempt {attempt} failed: {e}")

          if attempt < retries:
            print(f"[LOG] Retrying..\n")
            time.sleep(1)
          else: 
            print(f"[FAIL] All Retries exhausted\n")
            return None

    return wrapper       
  return decorator


@monitor(retries=3)  ## unstable_api_call  = monitor(retries=3)(unstable_api_call)
def unstable_api_call():
  import random

  if random.random() < 0.7:
    raise Exception("API Failed")

  return "Success!"

print(unstable_api_call())

## your function --> goes inside wrapper --> warpper has done