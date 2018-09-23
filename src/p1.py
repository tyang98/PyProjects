import random 
from builtins import list
def revDegs(number):
    if number < 10:
        print(number % 10, end="")
    else:   
        print(number % 10, end="" )
        revDegs(number // 10)

def reverse(s):
    if len(s) <= 1:
        return s
    
    left = s[0]
    right = reverse(s[1:])
    return right + left

def findLargeInt(lst):
    k = 1;
    large = lst[0]
    while k < len(lst):
        if lst[k] > large:
            large = lst[k]
        k = k + 1
    
    return large

coolList = [2, 10, 2, 6]
print(findLargeInt(coolList))