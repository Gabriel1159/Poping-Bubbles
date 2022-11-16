# 小型倒计时器
import time as t
import threading

time = 30 
time_out = False

def alarm_setter():
    global time
    global time_out
    while time > 0:
        t.sleep(1)
        time -= 1
    time_out = True

class MyThread(threading.Thread):
    def __init__(self, func):
        super(MyThread, self).__init__()
        self.func = func

    def run(self):
        self.func()


def main():
    num = 0
    alarm1 = MyThread(alarm_setter)
    alarm1.start()
    while num<=10000:
        print((time, time_out))
        num += 1

if __name__ == '__main__':
    main()