def solution(A):
    A.sort()
    for i in range(0, len(A)-2, 2):
        if A[i]!=A[i+1]:
            return A[i]
    return A[-1]


a = [5, 3, 1, 1, 2, 3, 2]
print(solution(a))