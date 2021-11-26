def solution(A):
    count = 0
    i = 0
    while(i<len(A)-1):
        car_idx = i
        while(car_idx<len(A)-1):
            car_idx += 1
            if(A[i]==0 and A[car_idx]==1):
                print([i, car_idx])
                count += 1
        i += 1
    return count


A = [0, 1, 0, 1, 1]

print(solution(A))
print(A)