def swap_solution(A, B):
    l = len(A)
    for i in range(l):
        A_ch = A.copy()
        B_ch = B.copy()
        A_ch[i], B_ch[i] = B_ch[i], A_ch[i]
        if sum(A_ch) == sum(B_ch):
            return True
    return False


a = [2, 2, 3,4]
b = [2, 2, 3, 5]
print(swap_solution(a, b))