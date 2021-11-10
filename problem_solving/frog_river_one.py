def solution(X, A):
    if len(set(A))<X:
        return -1
    B = [0]*len(A)
    sum = 0
    for i in range(len(A)):
        if A[i] <= X:
            if B[A[i]-1] == 0:
                B[A[i]-1] = 1
                sum += 1
            if sum==X:
                return i
    return -1

# def solution(X, A):
#     A_set = set(A)
#     n = len(A)
#     m = len(A_set)
#     # print(m)
#     if m < X:
#         # print('First case')
#         return -1
#     for i in range(n-X+1):
#         # print('second case')
#         # print(i, A[:X+i])
#         if A_set == set(A[:X+i]):
#             return X+i-1
#     # print('Third case')
#     return -1


# def solution(X, A):
#     A_set = set(A)
#     n = len(A)
#     m = len(A_set)
#     # print(m)
#     if m < X:
#         # print('First case')
#         return -1
#     i = 0
#     while i<n-X+1:
#         if A_set == set(A[:X+i]):
#             return X+i-1
#         i += 1
#     # print('Third case')
#     return -1
A = [4]
print(solution(5, A))
