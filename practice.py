#Challenge for data manipulation

AB7total = [100, 93, 85, 93, 95, 105, 85, 85, 86]
AB7Ram = [91, 85, 83, 90, 93, 97, 81, 82, 84]
ABAmo = [9, 8, 2, 3, 2, 8, 4, 3, 2]
ABAK7total = [115, 125, 200, 102, 175, 99, 151, 136, 109, 198, 84]
ABAK7Ram = [104, 112, 195, 98, 152, 82, 132, 121, 101, 169, 73]
ABAK7Amo = [11, 13, 15, 4, 23, 17, 19, 15, 8, 29, 11]

import statistics

def analytics(x):
    return ("avg =  " + str(sum(x) / len(x))), "n = " + str(len(x)), "stdev = " + str(statistics.stdev(x))
a = analytics(AB7total)
print(a)
b = analytics(AB7Ram)
print(b)
c = analytics(ABAmo)
print(c)
d = analytics(ABAK7total)
print(d)
