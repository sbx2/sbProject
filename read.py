import csv
from Date import Date
#open
def isNum(x):
    try:int(x)
    except:return 0
    return 1

# char(67) = 'C'
def rd(fn):
    res = []
    with open(fn, newline='\n') as csvin:
        data = csv.reader(csvin, delimiter=',')
        for row in data:
            
            res.append([int(x) if isNum(x) else x for x in row])
        return res

def zidian(c02cln):
#    c02cln = 15
    c02ttnum={}
    c02pd={}
    dictc02 = {}
    c02wt = rd('Deburrcopy.csv')[0][0]
    dt = rd('Deburrcopy.csv')[0][4:]
    for i in range(1,c02cln):
        #PD column  {1:}
        c02pd[i] = rd('Deburrcopy.csv')[i][1]
    for i in range(1,c02cln):
        # "# of wheels" total number for c02
        c02ttnum[i] = rd('Deburrcopy.csv')[i][2]
    for i in range(1,c02cln):
        # {346:30,331:28}
        dictc02[c02pd[i]] = c02ttnum[i]
        dictc02[c02wt] = c02pd
##      {total :[all date]}
        dictc02[c02ttnum[i]] = sum(rd('Deburrcopy.csv')[i][4:])
    return dictc02

    

    

for i in range(1,15):
    print(rd('Deburrcopy.csv')[i][4:])

#print(zidian(15))
