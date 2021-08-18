from threading import Thread, Event
import time as tm

class workCount(object):
    def __init__(self, cnt=0):
        self.cnt = cnt

    # def __bool__(self):
    #     return self.cnt > 0

    def clean(self):
        self.cnt = 0

    # def dec(self):
    #     self.cnt -= 1

    def inc(self):
        self.cnt += 1

    def wait(self, cnt, timeout=100000):
        while timeout > 0:
            timeout -= 1
            if self.cnt == cnt:
                return
            else:
                tm.sleep(0.001)
        raise TimeoutError("counter wait time out !!")
            

class swThread(Thread):
    def __init__(self, waitEvent, count, func=None, timeout=100):
        super().__init__()
        if func==None:
            self.func = self.dummyfunc
        else:
            self.func = func
        self.timeout = timeout
        self.count = count
        self.waitEvent = waitEvent

    def dummyfunc(self):
        return

    def run(self):
        while self.waitEvent.wait(self.timeout):
            self.waitEvent.clear()
            self.func()
            print("I am in {}".format(self.name))
            self.count.inc()
