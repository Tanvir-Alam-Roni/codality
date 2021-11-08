# def solution(X, Y, D):
#     jump = 0
#     while (X<Y):
#         X += D
#         jump += 1
#     return jump

def solution(X, Y, D):
    jump = ((Y-X) // D) + 1
    return jump


print(solution(10, 85, 30))
