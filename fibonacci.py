#!/usr/bin/python
new = 1
count = 10
old = 0

print("\n\nFibonacci number\n\n")

for i in range(count):
    new += old
    old = new - old
    print(new)
