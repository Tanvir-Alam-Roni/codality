def solution(A):
    dif = []
    if len(A)>1 :
        for p in range(1, len(A)):
            dif.append(abs(sum(A[:p]) - sum(A[p:])))
        return min(dif)
    return abs(A[0])

A = [3, 1, 2, 4, 3]
print(solution(A))
