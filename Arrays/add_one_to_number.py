'''
Given a non-negative number represented as an array of digits,

add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

Example:

If the vector has [1, 2, 3]

the returned vector should be [1, 2, 4]

as 123 + 1 = 124.


Average Time :- 43 min
Time Taken :- 22 min

'''

def plusOne(A):
    carry = 1

    # iterate over list from back and when carry will be 
    # 0 break from the loop because there no point of moving 
    # ahead as only 0 will be added from there
    for i in range(len(A)-1,-1,-1):
        value = A[i] + carry
        A[i] = value%10
        carry = value//10
        if carry == 0:
            break
    
    # if carry is greater then 0, then add it to head of the list
    # e.g in case of [9,9,9]
    if carry > 0:
        A.insert(0,carry)

    # remove all the leading 0s as o/p will not contain any leading 0s
    i= 0
    while A[i] == 0:
        del A[i]

    return A               

print(plusOne([9,9,9]))