import requests
from requests.exceptions import ConnectionError, ConnectTimeout
import time


def do_the_job():
    try:
        requests.get('http://185.110.189.178:8000/do_your_job_man')
        time.sleep(60)
        return True
    except (ConnectTimeout, ConnectionError):
        do_the_job()
    finally:
        return True


while True:
    do_the_job()
    time.sleep(1)
