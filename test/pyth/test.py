# import click
# import questionary


# class QuestionaryOption(click.Option):

#     def __init__(self, param_decls=None, **attrs):
#         click.Option.__init__(self, param_decls, **attrs)
#         if not isinstance(self.type, click.Choice):
#             raise Exception('ChoiceOption type arg must be click.Choice')

#     def prompt_for_value(self, ctx):
#         val = questionary.select(self.prompt, choices=self.type.choices).unsafe_ask()
#         return val

# @click.command()
# @click.option('--hash-type', prompt='Hash', type=click.Choice(['MD5', 'SHA1'], case_sensitive=False), cls=QuestionaryOption)
# def cli(**kwargs):
#     print(kwargs)


# if __name__ == "__main__":
#     cli()

# SuperFastPython.com
# example of pinging the status of a set of websites asynchronously
# from urllib.request import urlopen
# from urllib.error import URLError
# from urllib.error import HTTPError
# from http import HTTPStatus
# from concurrent.futures import ThreadPoolExecutor
# from concurrent.futures import as_completed
 
# # get the status of a website
# def get_website_status(url):
#     # handle connection errors
#     try:
#         # open a connection to the server with a timeout
#         with urlopen(url, timeout=3) as connection:
#             # get the response code, e.g. 200
#             code = connection.getcode()
#             return code
#     except HTTPError as e:
#         return e.code
#     except URLError as e:
#         return e.reason
#     except:
#         return e
 
# # interpret an HTTP response code into a status
# def get_status(code):
#     if code == HTTPStatus.OK:
#         return 'OK'
#     return 'ERROR'
 
# # check status of a list of websites
# def check_status_urls(urls):
#     # create the thread pool
#     with ThreadPoolExecutor(len(urls)) as executor:
#         # submit each task, create a mapping of futures to urls
#         future_to_url = {executor.submit(get_website_status, url):url for url in urls}
#         # get results as they are available
#         for future in as_completed(future_to_url):
#             # get the url for the future
#             url = future_to_url[future]
#             # get the status for the website
#             code = future.result()
#             # interpret the status
#             status = get_status(code)
#             # report status
#             print(f'{url:20s}\t{status:5s}\t{code}')
 
# # list of urls to check
# URLS = ['https://twitter.com',
#         'https://google.com',
#         'https://facebook.com',
#         'https://reddit.com',
#         'https://youtube.com',
#         'https://amazon.com',
#         'https://wikipedia.org',
#         'https://ebay.com',
#         'https://instagram.com',
#         'https://cnn.com']
# # check all urls
# check_status_urls(URLS)

import logging
import os
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from time import time

from download import setup_download_dir, get_links, download_link

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


def main():
    client_id = os.getenv('IMGUR_CLIENT_ID')
    if not client_id:
        raise Exception("Couldn't find IMGUR_CLIENT_ID environment variable!")
    download_dir = setup_download_dir()
    links = get_links(client_id)

    # By placing the executor inside a with block, the executors shutdown method
    # will be called cleaning up threads.
    # 
    # By default, the executor sets number of workers to 5 times the number of
    # CPUs.
    with ThreadPoolExecutor() as executor:

        # Create a new partially applied function that stores the directory
        # argument.
        # 
        # This allows the download_link function that normally takes two
        # arguments to work with the map function that expects a function of a
        # single argument.
        fn = partial(download_link, download_dir)

        # Executes fn concurrently using threads on the links iterable. The
        # timeout is for the entire process, not a single call, so downloading
        # all images must complete within 30 seconds.
        executor.map(fn, links, timeout=30)


if __name__ == '__main__':
    main()
