def solution(A):
    A.sort()
    A = list(set(A))
    i = 0
    if A[0]>1:
        return 1
    while(i < len(A)-1):   
        if (A[i]<0 and A[i+1]>1):
            return 1
        if(A[i]>=0 and A[i+1] != A[i]+1):
            return A[i]+1         
        i += 1
    if A[i]<0:     
        return 1  
    return A[i]+1

A = [0, 2, 1000]        
print(solution(A))