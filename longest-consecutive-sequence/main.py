import unittest

def solve(A):
    n = len(A)

    if n < 2: 
        return 1
    else: 
        a_set = set(A)
        longest = 1
        for i in A:
            # check i - 1 is in set?
            if i - 1 in a_set:
                longest += 1
        return longest


if __name__ == '__main__': 
    A = [2]
    assert solve(A) == 1   
    A = [2,4]
    assert solve(A) == 1  
    A = [7,100,6,5,2,1]
    assert solve(A) == 4
    B = [100,4,200,1,3,2]
    assert solve(B) == 4
    C = [0,3,7,2,5,8,4,6,0,1]
    assert solve(C) == 9