import time

import threading


class TestThreading(object):
    def __init__(self, interval=1):
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            # More statements comes here
            print(str(time.time()) + ' : Start task in the background')

            time.sleep(self.interval)

tr = TestThreading()
time.sleep(1)
print(str(time.time()) + ' : First output')
time.sleep(2)
print(str(time.time()) + ' : Second output')