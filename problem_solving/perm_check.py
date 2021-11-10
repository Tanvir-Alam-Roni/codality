def solution(A):
    n = len(A)
    perm = set(range(1, n+1))
    if set(A)==perm:
        return 1
    return 0

A = [0]
print(solution(A))
# print(list(range(1, 5)))