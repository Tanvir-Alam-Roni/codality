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

# def solution(A):
#     if len(A)>1 :
#         p = 1
#         m = float('inf')
#         while p < len(A):
#             m = min((abs(sum(A[:p]) - sum(A[p:]))), m)    
#         return min
#     return abs(A[0])

def solution(A):
    if len(A)>1 :
        s = sum(A)
        left_sum = 0
        m = float('inf')
        for el in A[:-1]:
            m = min(abs(sum(s - 2*left_sum)), m)
        return m
    return abs(A[0])
A = [3]
print(solution(A))
