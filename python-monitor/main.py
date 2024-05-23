import requests,validators, threading
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

def get_stt(u):
    # try:
    result = requests.get(u, timeout=10)
    if(result.status_code == 200):
        print("webiste connected")
    else:
        print("website disconnected")
    # except:
    #     print("No website in the monitoring list")

if __name__ == "__main__":
    while True:
        with open("url.txt", 'a+') as f:
            url = add_website()
            f.writelines(url+"\n")
            confirm = input('Continue ? [Y/N] ')
            if confirm in ('y', 'yes', 'Y'):
                continue
            elif confirm in ('n', 'no', 'N'):
                opt = input('Check ? [Y/N] ')
                if opt in ('y', 'yes', 'Y'):
                    with open("url.txt", 'r') as f:
                        for u in f:
                            get_stt(u)
                        # for i in u:
                        #     num_thread = 5
                        #     with ThreadPoolExecutor(max_workers = num_thread) as executor:
                        #         executor.map(get_stt, u)
                else:
                    continue
            else:
                break
            break
