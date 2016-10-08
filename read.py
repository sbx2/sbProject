import csv
#open
def isNum(x):
    try:int(x)
    except:return 0
    return 1
def rd(fn):
    res = []
    with open(fn, newline='\n') as csvin:
        c02data = csv.reader(csvin, delimiter=',')
        for row in c02data:
            res.append([int(x) if isNum(x) else x for x in row ])
    return res

            
#def wt():
#    with open('testout.csv', 'w') as csvout:
#        writer = csv.writer(csvout);
#        for row in writer:
#            writer.writerow(row+['FFF']);
#    return;

y = rd('test.csv')
print(y[0][0])
