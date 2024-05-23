import requests, validators, threading
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

def add_website():
    url = str(input("Add: "))
    if validators.url(url) != True:
        print("Invalid input")
        pass
    elif len(url) > 1000:
        print("url too long")
    else:
        print("Website %s added to the monitoring list" % (url))
    return url

def get_stt():
    result = requests.get()
    try:
        if(result.status_code == 200):
            print("webiste is connected")
        else:
            print("website is disconnected")
    except:
        print("No websites in the monitoring list")
        time.sleep(2)

# def remove_website():

