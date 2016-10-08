import sys
sys.path.append('..')
from Date import Date
def read(fn):
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
                tem[header[i]]=row[i]
            dt[row[1]] = tem
        res[wt] = dt        
    f.close()

