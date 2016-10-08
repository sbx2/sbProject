
class Date:
    def __init__(self,y=0,m=0,d=0,**dic):
        if not len(dic):
            self.y = y
            self.m = m
            self.d = d
        else:
            d = dic['date']
            self.d = int(d[:d.index('-')])
            d = d[d.index('-')+1:]
            self.m = strptime(d[:d.index('-')],'%b').tm_mon 
            self.y = int(d[d.index('-')+1:])
    def isLeapY(self):
        return not(self.y%400)or((not(self.y%4))and(self.y%100))
    def ttnm(self):
        if(self.m==2):
            return(29 if self.isLeapY() else 28)-self.d+1
        if((self.m%2)and(self.m<8))or((not self.m%2)and(self.m>7)):
            return 31-self.d+1
        if((not self.m%2)and(self.m<8))or((self.m%2)and(self.m>7)):
            return 30-self.d+1
    def ttny(self):
        dd = 366 if self.isLeapY() else 365
        dd = dd-self.d
        for i in range(1,self.m):
            dd = dd - Date(self.y,i,1).ttnm()
        return dd+1
    def __add__(self,b):
        if not isinstance(b,(int,float)):
            return -1
        dd = int(b)
        res = Date(self.y,self.m,self.d)
        while dd >= res.ttny():
            dd = dd-res.ttny()
            res.y += 1
            res.m = 1
            res.d = 1
        while dd >= res.ttnm():
            dd = dd-res.ttnm()
            res.m += 1
            res.d = 1
        res.d += dd
        return res
    def __eq__(self,oth):
        return (self.y==oth.y) and (self.m==oth.m) and (self.d==oth.d)
    def __gt__(self,oth):
        if self.y!=oth.y:
            return self.y>oth.y
        if self.m!=oth.m:
            return self.m>oth.m
        if self.d!=oth.d:
            return self.d>oth.d
        return False
    def __lt__(self,oth):
        if self!=oth:
            return not self>oth
        return False
    def __le__(self,oth):
        return self<oth or self==oth
    def __ge__(self,oth):
        return self>oth or self==oth
    def __ne__(self,oth):
        return not self==oth
    def __sub__(self,oth):
        if type(oth)==int:
            res = Date(self.y-int(oth/365)-1,1,1)
            while res+oth!=self:
                res += 1
            return res
        if self<=oth:
            return -1
        b = oth
        res = 0
        while b<self:
            tny = b.ttny()
            b+=tny
            res+=tny
        while b>self:
            b-=1
            res-=1
        return res
    def __str__(self):
        return str(self.y)+"."+str(self.m)+"."+str(self.d)
    def __repr__(self):
        return self.__str__()
