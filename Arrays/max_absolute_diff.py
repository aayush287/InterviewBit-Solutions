'''
 Average Time : 65 min
 Time Taken : 14 min
'''

def maxArr(A):
    max1 = -10000000000005
    min1 = 10000000000005
    max2 = -10000000000005
    min2 = 10000000000005
    for i in range(len(A)):
        max1 = max(max1, A[i]+i)
        min1 = min(min1, A[i]+i)
        max2 = max(max2, A[i]-i)
        min2 = min(min2, A[i]-i)
    
    return max(abs(max1-min1), abs(max2-min2)) 

print(maxArr([1, 3, -1]))