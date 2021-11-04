import requests
import time

def calculate_time():
    begin= time.time()
    response = requests.get('https://imdb.com/')
    time.sleep(1)
    end = time.time()
    print(f"Total runtime of the program is {end - begin}")

calculate_time()