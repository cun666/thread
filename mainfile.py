from workThread import swThread, workCount
import threading
import time as tm

def myprint():
    tm.sleep(0.01)
    # print(strparam)

threadcnt = 3
if __name__ == "__main__":
    imgreadyEvent = threading.Event()
    swcount = workCount(0)
    threadlist = []
    for i in range(threadcnt):
        threadlist.append(swThread(imgreadyEvent, swcount, myprint))

    for thread in threadlist:
        thread.setDaemon(True)
        thread.start()

    for i in range(20):
        print("img ready !!")
        imgreadyEvent.set()
        swcount.wait(threadcnt)
        swcount.clean()