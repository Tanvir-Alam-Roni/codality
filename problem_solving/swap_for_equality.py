# O(n^3)
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

# O(n^2)
def slow_solution(A, B):
    l = len(A)
    sum_a = sum(A)
    sum_b = sum(B)
    for i in range(l):
        for j in range(l):
            change = B[j] - A[i]
            sum_a += change
            sum_b -= change
            if sum_a == sum_b:
                return True
            sum_a -= change
            sum_b += change
    return False


a = [4, 2, 2, 3, 1]
b = [2, 2, 2, 3, 5]
print(slow_solution(a, b))