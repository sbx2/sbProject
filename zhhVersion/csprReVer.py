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
        self.wtList = []
        self.res = {}
        for table in t:
            trs = table.split('\n')
            header = trs[0].split(',')
            wt = header[0]
            dt = {}
            for row in trs[1:]:
                row = [num(x) for x in row.split(',')]
                tem = {}
                for i in range(2,len(header)):
                    try:tem[header[i]]=row[i]
                    except:continue
                try:dt[row[1]] = tem
                except:continue
            self.header = header[4:]
            self.res[wt]=dt
            self.wtList.append(wt)
        self.wtList.sort()
        self.header.sort(key = lambda x:int(x.split('-')[0]))
        f.close()
    def addPD(self,wt,pd):
        self.res[wt][pd] = {}
        for i in self.header:
            self.res[wt][pd][i] = 0
            self.res[wt][pd]['Ratio'] = 0
    def setVal(self,wt,pd,dt,val):
        self.res[wt][pd][dt] = val
    def calcTotalW(self):
        for wt in self.res:
            for pd in self.res[wt]:
                self.res[wt][pd]['# of wheels'] = sum([self.res[wt][pd][d] for d in self.header])
    def calcTotalD(self):
        for wt in self.res:
            self.res[wt]['dailyTotal'] = {}
            for h in self.header:
                self.res[wt]['dailyTotal'][h] = sum([self.res[wt][pd][h] if pd !='dailyTotal' else 0 for pd in self.res[wt]])
    def oup(self,fn,dli = ''):
        f = open(fn,'w')
        for wt in self.wtList:
            row0 = dli+wt+',Problem Description,# of wheels,Ratio,'+','.join(self.header)
            rows = []
            pdList = [pd if type(pd)==int else None for pd in self.res[wt]]
            for pd in pdList:
                try:rows.append([self.res[wt][pd]['# of wheels'],','+str(pd)+','+str(self.res[wt][pd]['# of wheels'])+','+str(self.res[wt][pd]['Ratio'])+','+','.join([str(self.res[wt][pd][h]) for h in self.header])])
                except:continue
            rows.sort(key = lambda x:x[0],reverse = True)
            rows = [row[1] for row in rows]
            f.writelines(row0+'\n')
            f.writelines('%s\n'%line for line in rows)
            datot = [self.res[wt]['dailyTotal'][h] for h in self.header]
            rowf = ',Total,'+str(sum(datot))+',0,'+','.join([str(x) for x in datot])
            f.writelines(rowf+'\n')
        f.close()

#a = CSreportController('../DeBurr.csv')
#a.addPD('C15',4322)
#a.calcTotalW()
#a.calcTotalD()
#print(a.header)
#a.oup('oup.csv')
