import sys
sys.path.append('..')
from Date import Date
def readCSV(fn):
    f = open(fn)
    t = f.read().split(chr(477))
    res = {}
    for table in t:
        trs = table.split('\n')
        header = trs[0].split(',')
        wt = header[0]
        dt = {}
        for row in trs[1:]:
            row = row.split(',')
            tem = {}
            for i in range(2,len(header)):
                try:tem[header[i]]=row[i]
                except:continue
            try:dt[row[1]] = tem
            except:continue
        res['header'] = header[2:]
        res[wt] = dt
    f.close()
    return res
def addPD(table,wt,pd):
    table[wt][pd] = {}
    for i in table['header']:
        table[wt][pd][i] = ''
def setVal(table,wt,pd,dt,val):
    table[wt][pd][dt] = val
def isNum(x):
    try:int(x)
    except:return 0
    return 1
def calcNoWs(table,wt,pd):
    table[wt][pd]['# of wheels']=sum([int(table[wt][pd][d]) if d!='# of wheels' and isNum(table[wt][pd][d]) else 0 for d in table[wt][pd]])


r = readCSV('../Deburr.csv')
addPD(r,'C02','111')
setVal(r,'C02','111','8-Sep','26')
calcNoWs(r,'C02','346')
print(r['C02']['346']['# of wheels'] )
