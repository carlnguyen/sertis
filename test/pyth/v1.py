import requests, validators, threading

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
    url = add_website()
    thelist = []
    thelist.append(url)
    for i in thelist:
        result = requests.get(i)
        try:
            if(result.status_code == 200):
                print("webiste %s is connected" % (i))
            else:
                print("website %s s disconnected" % (i))
        except:
            print("No websites in the monitoring list")
            time.sleep(2)

if __name__ == "__main__":
    get_stt()
    # threads = [threading.Thread(target=get_stt, args=(url,)) for url in listurl]
    # for thread in threads:
    #     thread.start()
    # for thread in threads:
    #     thread.join()
