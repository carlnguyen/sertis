import requests, validators, threading, click

# remove_url = input("Remove: ")
# check = input("Check")

# @click.command()
# @click.option("--url", prompt="Add: ",help="Add a new website to monitoring list")
# def add_website(url):
#     if len(url) > 1000:
#         click.echo("Your url too long")
#     else:
#         click.echo(f"Website {url} added to the monitoring list")
#         return url

def add_website():
    url = str(input("Add: "))
    listurl = []
    if validators.url(url) != True:
        print("Invalid input")
        pass
    elif len(url) > 1000:
        print("url too long")
    else:
        listurl.append(url)
        print("Website %s added to the monitoring list" % (url))
    return listurl

def get_stt():
    urls = add_website()
    for i in urls:
        result = requests.get(i)
        try:
            if(result.status_code == 200):
                print("webiste %s is connected" % (i))
            else:
                print("website %s s disconnected" % (i))
        except:
            print("No websites in the monitoring list")
            time.sleep(2)

    #try:
    #    get = requests.get(url)
    #    if get.status_code == 200:
    #        return(f"{url}: is reachable")
    #    else:
    #        return(f"{url}: is Not reachable, status_code: {get.status_code}")

    ##Exception
    #except requests.exceptions.RequestException as e:
    #    # print URL with Errs
    #    raise SystemExit(f"{url}: is Not reachable \nErr: {e}")

    # url=add_website(url)
    # result = requests.get(url)
    # method = result.request.method
    # return (result.status_code == 200, method)

if __name__ == "__main__":
    get_stt()
                # @click.command()
            # @click.option(
            #         prompt="next_action", type=click.Choice(['check','remove'])
            #         )
            # if next_action == 'check':
            #     get_stt()
            # else:
            #     break

    # get_stt()
    # urls = usr_input()
    # print("Website", urls, "added to the monitoring list")

    # threads = [threading.Thread(target=get_stt, args=(url,)) for url in urls]
    # for thread in threads:
    #     thread.start()
    # for thread in threads:
    #     thread.join()
