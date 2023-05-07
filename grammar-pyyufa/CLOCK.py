'''import time
import os

class clock():
    def __init__(self,h,m,s):
        self.hour=h
        self.minute=m
        self.second=s
    
    def run(self):
        
            self.second+=1
            if self.second==60 and self.minute<60:
                self.minute+=1
                self.second=0
                if self.minute==60 and self.hour<24:
                    self.hour+=1
                    self.minute=0
                    if self.hour==24:
                        self.hour=0
    
    def timeis(self):
         print("%.2d:%.2d:%.2d"%(self.hour,self.minute,self.second))

if __name__=='__main__':
    clock1=clock(12,9,20)
    while True:
        clock1.timeis()
        time.sleep(1)
        clock1.run()
        os.system('cls')
        '''
from time import time, localtime, sleep


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()