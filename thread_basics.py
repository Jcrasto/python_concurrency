import time
import threading
from threading import Thread


class MyThread(Thread):
    def __init__(self, time_to_sleep, name=None):
        super().__init__(name=name)
        self.time_to_sleep = time_to_sleep

    def run(self):
        ident = threading.get_ident()
        print(f"I am thread {self.name} (ID {ident}), and I'm sleeping for {self.time_to_sleep} secs.")
        time.sleep(self.time_to_sleep)
        print(f'Thread {self.name} exiting ...')


def simple_worker(time_to_sleep):
    myself = threading.current_thread()
    ident = threading.get_ident()
    print(f"I am thread {myself.name} (ID {ident}), and I'm sleeping for {time_to_sleep} secs.")
    time.sleep(time_to_sleep)
    print(f'Thread {myself.name} exiting ...')

if __name__ == "__main__":
    t1=Thread(target=simple_worker, name = 'Squirtle', args = (3,))
    t2 = Thread(target =simple_worker, name = 'Bulbasaur', args = (1.5,))
    t3 = Thread(target =simple_worker, name = 'Charmander', args = (2,))
    t1.start()
    t2.start()
    t3.start()

    t = MyThread(2)
    t.start()
