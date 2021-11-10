# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    x = [0]*N
    for el in A:
        if el>N:
            x = [max(x)]*N
        elif el >= 1 and el <= N:
            x[el-1] += 1
    return x