from math import log

number = int(input())
base = int(input())

if base <= 1:
    print(round(log(number), 2))
else:
    print(round(log(number, base), 2))
