def solution(A):
    # write your code in Python 3.6
    A.sort()
    for i in range(len(A)):
        if A[i] != i+1:
            return i+1

A = [2, 3, 1, 5, 6, 7, 9, 4]

print(solution(A))
