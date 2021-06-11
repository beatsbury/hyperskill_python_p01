# put your python code here
from math import sqrt

input1 = int(input())
input2 = int(input())
input3 = int(input())

p = (input1 + input2 + input3) / 2
s = sqrt(p * (p - input1) * (p - input2) * (p - input3))

print(s)
