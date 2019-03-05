#!/usr/bin/python
import time
print(time.process_time())

def absolute(num):

    res = 0

    for i in range(1, num):

        if(num % i == 0):

            res += i

    return res

#----------------------------------------------

def search(num):

    res = absolute(num);

    if (absolute(res) == num):

        return res;

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
print(time.process_time())
