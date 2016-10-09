import sys
sys.path.append('..')
from Date import Date
def num(x):
    try:return int(x)
    except:return 0
class CSreportController:
    def __init__(self,fn,dli = 477):
        f = open(fn)
        t = f.read().split(chr(dli))
        self.res = {}
        for table in t:
            trs = table.split('\n')
            header = trs[0].split(',')
            wt = header[0]
            dt = {}
            for row in trs[1:]:
                row = [num(x) for x in row.split(',')]
                #row = row.split(',')
                tem = {}
                for i in range(2,len(header)):
                    try:tem[header[i]]=row[i]
                    except:continue
                try:dt[row[1]] = tem
                except:continue
            self.header = header[3:]
            self.res[wt]=dt
        f.close()
    def addPD(self,wt,pd):
        self.res[wt][pd] = {}
        for i in self.header:
            self.res[wt][pd][i] = 0
    def setVal(self,wt,pd,dt,val):
        self.res[wt][pd][dt] = val
    def calcNoW(self,wt,pd):
        self.res[wt][pd]['# of wheels'] = sum([self.res[wt][pd][d] for d in self.header])

a = CSreportController('../DeBurr.csv')
a.addPD('C02',1000)
a.setVal('C02',1000,a.header[3],231)
for x in a.res['C02']:
    print(x,a.res['C02'][x])
