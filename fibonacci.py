#!/usr/bin/python
new = 1
count = 10
old = 0

print("\n\nFibonacci number\n\n")
#count = input("dose no numero: ")
"""
for w in range(count):
    res = new + old
    old = new
    new = res
    print(new)
"""

for i in range(count):
    new += old
    old = new - old
    print(new)
