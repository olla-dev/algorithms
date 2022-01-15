import unittest

def solve(A):
    n = len(A)
    if n == 1: 
        return 1

    max_volume = 0

    i = 0
    j = n - 1

    while i < j:
        max_volume = max(max_volume, min(A[i], A[j]) * (j-i))

        if A[i] < A[j]:
            i += 1
        else:
            j -= 1

    return max_volume

if __name__ == '__main__': 
    A = [1,8,6,2,5,4,8,3,7]
    assert solve(A) == 49  
    A = [1,1]
    assert solve(A) == 1
    