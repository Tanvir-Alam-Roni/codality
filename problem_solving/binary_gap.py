def solution(n):
    b = bin(n)[2:]
    print(b)
    gaps = []
    l = len(b)
    i = 0
    count = 0
    start_flag = 0
    while(i<l):
        if(b[i]=='1' and start_flag==1):
            gaps.append(count)
            start_flag = 0
        if(b[i]=='1' and start_flag==0):
            start_flag = 1
            count = 0
        if(b[i]=='0' and start_flag==1):
            count += 1
        i += 1
    if len(gaps)>0:
        return max(gaps)
    else:
        return 0


n = 1041
sample = '0001001000100001000'

print(solution(n))