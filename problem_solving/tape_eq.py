# def solution(A):
#     dif = []
#     if len(A)>1 :
#         for p in range(1, len(A)):
#             dif.append(abs(sum(A[:p]) - sum(A[p:])))
#         return min(dif)
#     return abs(A[0])


# def solution(A):
#     dif = []
#     if len(A)>1 :
#         p = 1
#         while p < len(A):
#             dif.append(abs(sum(A[:p]) - sum(A[p:])))
#             p += 1
#         return min(dif)
#     return abs(A[0])

def solution(A):
    if len(A)>1 :
        p = 1
        min = 999999999999999
        while p < len(A):
            dif = (abs(sum(A[:p]) - sum(A[p:])))
            if dif<min:
                min = dif
            p += 1
        return min
    return abs(A[0])
A = [3]
print(solution(A))
