#trying something new

from random import *
from math import *
import os
import time

a = random.randint(3,9)
b = random.randint(3,9)
n=int(input("please enter the number of repetitions: "))
if type(n) != int:
    print("invalid output")
print("value of a: ", a)
print("value of b: ", b)

c = (a+b)/2

for i in range(2,n):
    if n%i==0:
        print("not a prime number")
    else:
        print("prime number")
    i+=1

print(type(1))
print(type(3.14))
