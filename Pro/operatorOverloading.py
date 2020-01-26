class Point:
    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r=r
    def __str__(self):
        return "({0},{1},{2})".format(self.x,self.y,self.r)
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        r=self.r+other.r
        return Point(x,y,r)
p1=Point(2,3,6)
p2=Point(1,2,3)
print(p1+p2)
