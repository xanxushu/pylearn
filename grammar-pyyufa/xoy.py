import math

class xoy(object):
    def __init__(self,xx,yy):
        self.x=xx
        self.y=yy
    
    def distance(self,other):
        dx=math.sqrt((self.x-other.x)*(self.x-other.x))
        dy=math.sqrt((self.y-other.y)*(self.y-other.y))
        dis=math.sqrt(dx**2+dy**2)
        return dis

if __name__=='__main__':
    xoy1=xoy(2,-2)
    xoy2=xoy(-1,2)
    print(xoy1.distance(xoy2))
