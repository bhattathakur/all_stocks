#!/bin/python3
#This program calculates the % of a stock above and below the given values

import numpy as np

value=float(input("INPUT VALUE: "))*100

print(f"INPUT VALUE: {value:0.2f}\n")

ptrstr=33*"="


for i in range(1,26):
    if i in [1]:print(ptrstr);print(f"|  -%\t        %\t+%      |");print(ptrstr)

    print(f"|  {(1-i/100)*value:0.2f}\t{i}\t{(1+i/100)*value:0.2f}  |")
    if i in[25]:print(ptrstr)
print()


