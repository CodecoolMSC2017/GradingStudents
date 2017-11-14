#!/bin/python3

import sys

def solve(grades):
    sor = []
    for i in grades:
        if i < 38:
            sor.append(i)
        elif i >= 38:            
            i_rounded = int(round(i/5.0)*5)
            if i_rounded - i <= 3:
                sor.append(i_rounded)
            elif i_rounded - i == 3:
                sor.append(i)
            else:
                sor.append(i)
    return sor
            
n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
