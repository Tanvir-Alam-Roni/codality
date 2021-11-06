def solution(N):
    n_bin = bin(N).split('b')[1]
    digits = n_bin.split('1')
    l = [len(s) for s in digits]
    return max(l)

print(solution(32))

