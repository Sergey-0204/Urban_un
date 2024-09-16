from threading import Thread

import requests


class Getter(Thread):
    res = []
    THE_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'

    def run(self):
        response = requests.get(self.THE_URL)
        Getter.res.append(response.json())


threads = []

for i in range(10):
    thread = Getter()
    thread.start()
    threads.append(thread)

    for thread in threads:
        thread.join()
