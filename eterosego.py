#----------------------------------------------
# Kav and Xristos
#----------------------------------------------
def absolute(num):
    res = 0
    for i in range(1, num):
        if(num % i == 0):
            res += i
    return res
#----------------------------------------------
#  Main
#----------------------------------------------
limit = int(input("Dose ena arithmo: "))
res = 0
for i in range(1, limit):
    res = absolute(i);
    if (absolute(res) == i and res != i):    
        print(i, res)
