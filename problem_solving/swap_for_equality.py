def swap_solution(A, B):
    l = len(A)
    for i in range(l):
        for j in range(l):
            A_ch = A.copy()
            B_ch = B.copy()
            A_ch[i], B_ch[j] = B_ch[j], A_ch[i]
            if sum(A_ch) == sum(B_ch):
                print(i, j)
                print(A_ch, B_ch)
                return True
    return False


a = [4, 2, 2, 3, 1]
b = [2, 2, 2, 3, 5]
print(swap_solution(a, b))