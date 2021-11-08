# def solution(A):
#     # write your code in Python 3.6
#     A.sort()
#     for i in range(len(A)):
#         if A[i] != i+1:
#             return i+1

def solution(A):
    # write your code in Python 3.6
    if len(A)>0:
        A.sort()
        i = 0
        while(i<len(A)):
            if A[i] != i+1:
                return i+1
            i += 1
    return 1
    
A = []

print(solution(A))
