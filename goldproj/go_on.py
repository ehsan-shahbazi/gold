import requests
import time

while True:
    time.sleep(60)
    requests.get('http://185.110.189.178:8000/do_your_job_man')
