import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *
import time

PROJECT_NAME = 'Gik'
HOMEPAGE = 'https://www.giki.edu.pk/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'

NUMBER_OF_THREADS = 8
queue = Queue()
x = Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)
QUEUE = x.crawl_page('First spider', HOMEPAGE)
# Create worker threads (will die when main exits)


def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do the next job in the queue
def work():
    global QUEUE
    while True:
        url = queue.get()
        QUEUE = Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# Each queued link is a new job
def create_jobs():
    for link in QUEUE:
        queue.put(link)
    queue.join()
    crawl()


# Check if there are items in the queue, if so crawl them
def crawl():
    global QUEUE
    #queued_links = file_to_set(QUEUE_FILE)
    if len(QUEUE) > 0:
        print(str(len(QUEUE)) + ' links in the queue')
        create_jobs()
    else:
        print('Crawling completed')


start = time.time()
create_workers()
crawl()
end = time.time()
print(f'time taken = {end-start}.')
