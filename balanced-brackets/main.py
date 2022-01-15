import unittest

def solve(A):
    n = len(A)
    if n < 1: 
        return 'NO'
    
    stack = []
    opening = ['{', '(', '[']
    closing = ['}', ')', ']']
    
    for i in A:
        if i in opening:
            stack.append(i)
        if i in closing:
            if len(stack) == 0 or closing.index(i) != opening.index(stack[-1]):
                return 'NO'
            stack.pop()

    return 'YES' if len(stack) == 0 else 'NO'

if __name__ == '__main__': 
    A = ['{','[','(',')',']','}']
    assert solve(A) == 'YES' 
    A = ['{','[','(',']',')','}']
    assert solve(A) == 'NO'
    A = ['[','(',']',')']
    assert solve(A) == 'NO'
    A = ['{','{','[','[','(','(',')',')',']',']','}','}']
    assert solve(A) == 'YES'