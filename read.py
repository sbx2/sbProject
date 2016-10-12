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
    c02ttnum=[]
    c02pd=[]
    c02wt = rd('Deburrcopy.csv')[0][0]
    dt = rd('Deburrcopy.csv')[0][4:]
    for i in range(1,c02cln):   #PD column
        c02pd.append(rd('Deburrcopy.csv')[i][1])
    for i in range(1,c02cln):   # "# of wheels" total number for c02
        c02ttnum.append(rd('Deburrcopy.csv')[i][2])
    dictc02 = {c02wt:c02pd}     #dictionary
    for i in range(0,c02cln-1): # {'C02':[346..352]}
        dictc02[c02pd[i]] = c02ttnum[i]
    for i in range(1,c02cln-1): # {total :[all date]}
        dictc02[c02ttnum[i-1]] = rd('Deburrcopy.csv')[i][4:]
    return dictc02

    

    


#print(rd('Deburrcopy.csv')[0][0])
print(zidian(15))
