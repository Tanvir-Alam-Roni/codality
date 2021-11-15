# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    x = [0]*N
    m = 0
    for el in A:
        if el == N+1:
            x = [m]*N
        elif el >= 1 and el <= N:
            x[el-1] += 1
            if x[el-1]>m:
                m = x[el-1]
    return x