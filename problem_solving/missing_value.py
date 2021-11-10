def solution(A):
    flag = 0
    i = 1
    while flag==0:
        if i not in set(A):
            return i
        i += 1

A = list(range(100))

print(solution(A))