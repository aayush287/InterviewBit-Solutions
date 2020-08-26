'''
Average Time :- 55 min
Time taken :- 32 min
'''
def solve(A, B):
    list_sum = 0
    for i in range(A):
        list_sum += B[i]
    if list_sum%3 != 0:
        return 0     
    quo = list_sum//3
    ans = 0
    count = 0
    s = 0
    for i in range(A-1):
        s += B[i]
        if s == 2*quo:
            ans += count
        if s == quo:
            count +=1
    return ans    

print(solve(4,[0,1,-1,0]))        