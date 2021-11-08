# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):       # A --> 1, 2, 3, 4   K --> 2   
    # write your code in Python 3.6
    if len(A)>1:
        for k in range(K):                      # k = 0
            temp = A[-1]                        # temp=4
            for i in range(len(A)-1, 0, -1):       # i = 1
                A[i] = A[i-1]                      # 1, 1, 2, 3
                print(i)
            A[0] = temp                         # 4, 1, 2, 3
            print(i)
        return A
    return A

print(solution([], 1))
