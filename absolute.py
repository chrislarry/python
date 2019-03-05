#!/usr/bin/python
def absolute(num):
    res = 0
    for i in range(1, num):
        if(num % i == 0):
            res += i
#        print(i)
    return res
#----------------------------------------------
print("-------------")
num = int(input("Dose ena arithmo: "))
res = 0
res = absolute(num)
print(res)
print("-------------")


