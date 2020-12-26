def flip(A):
    no_of_zeroes = 0
    l = 0
    result = []
    max_sum = 0

    for i in range(len(A)):
        if A[i] == '0':
            no_of_zeroes += 1

            if no_of_zeroes > max_sum:
                max_sum = no_of_zeroes
                result = [l+1, i+1]
        else:
            no_of_zeroes -= 1
            if no_of_zeroes < 0:
                l = i + 1
                no_of_zeroes = 0
    return result

print(flip('010'))        