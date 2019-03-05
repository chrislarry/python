#!/usr/bin/python
#-------kav---------xristos--------------------
#----------------------------------------------
def absolute(num):
    res = 0
    for i in range(1, num):
        if(num % i == 0):
            res += i
    return res
#----------------------------------------------
def search(num):
    for i in range(1, num):
        if (absolute(i) == num and absolute(num) == i):
            return i;
#----------------------------------------------
#  ----- Main
#----------------------------------------------
print("-------------")
limit = int(input("Dose ena arithmo: "))
res = 0
for i in range(1, limit):
    res = search(i)
    if(res != None):
        print(i, res)


