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
        res[wt] = dt        
    f.close()

    return res
r = readCSV('../Deburr.csv')
print(r['C12']['344']['14-Sep'])
