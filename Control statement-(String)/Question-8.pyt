# given an array of integers A sum array often array a to be good if it full fills any one of the critiarea
# len of the sum even and the sum of all the element of the sum array must be <b
# len of the sum odd and the sum of all the element of the sum array must be >b array must be <b you need the find sum of good array in a
# len of array-j-i+1
def count_good_subarrays(A, B):
    n = len(A)
    count = 0

    for i in range(n):
        total = 0
        for j in range(i, n):
            total += A[j]
            length = j - i + 1
            if (length % 2 == 0 and total < B) or (length % 2 == 1 and total > B):
                count += 1
    return count

