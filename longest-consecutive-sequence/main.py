import unittest

def solve(A):
    a_set = set(A)
    longest = 0
    for i in A:
        # check i - 1 is in set?
        if i - 1 not in a_set:
            j = i
            while j in a_set:
                j += 1
            longest = max(longest, j - i)
    return longest


if __name__ == '__main__': 
    A = [2]
    assert solve(A) == 1   
    A = [2,4]
    assert solve(A) == 1  
    A = [7,100,6,5,2,1,3]
    assert solve(A) == 3
    B = [100,4,200,1,3,2]
    assert solve(B) == 4
    C = [0,3,7,2,5,8,4,6,0,1]
    assert solve(C) == 9