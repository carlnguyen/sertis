import click
from monitor import add_website
from monitor import get_stt
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed


@click.command()
@click.option('--action', prompt='Choose option: ', type=click.Choice(['Add','Check','Remove'], case_sensitive=False))
def get_action(action):
    thelist = []
    if action == "Add":
        url = add_website()
        thelist.append(url)
        print(thelist)
    # elif action == "Check":
    #     for i in thelist:
    #         get_stt(i)

    return action

if __name__ == "__main__":
    action = get_action()
    with ThreadPoolExecutor(len(thelist)) as executor:
        for url in thelist:
            future_to_url = {executor.submit(get_stt, url)}
            for future in as_completed(future_to_url):
                url = future_to_url[future]
                code = future.result()
                print("Website %s is connected")

