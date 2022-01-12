import unittest

def solve(arr):
    n = len(arr)
    min_length = 2
    
    if n <= 1:
        return 1
    if n == 2:
        return 2
    else:
        l = min_length
        for i in range(2, n):
            if arr[i - 2] == arr[i]:
                l += 1
                min_length = max(min_length, l)
            else:
                l = 2
    return min_length

if __name__ == '__main__':    
    A = [2]
    assert solve(A) == 1   
    A = [2,4]
    assert solve(A) == 2   
    A = [2,4,2,4]
    assert solve(A) == 4
    B = [3,7,3,7, 2, 1, 2]
    assert solve(B) == 4
    C = [1,5,6,0,1,0]
    assert solve(C) == 3
    D = [7,-5,-5,-5,7,-1,7]
    assert solve(D) == 3