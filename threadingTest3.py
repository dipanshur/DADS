import threading
import time

def call_api(api_name):
    print(f"Calling {api_name}")
    time.sleep(2)
    print(f"{api_name} response recived")

apis = ["Auth", "Payments", "Orders"]

threads = []

for api in apis:
    t = threading.Thread(target=call_api, args=(api,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All API calls completed")




