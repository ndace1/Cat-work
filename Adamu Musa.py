def merge(A, p, q, r):
    #split the array and create temporary arrays for left and right parts
    leftPart = A[p:q + 1]      # A[p..q]
    rightPart = A[q + 1:r + 1] # A[q+1..r]

    i = 0  # leftPart Index
    j = 0  # rightPart index
    k = p  # merged array in A index

    while i < len(leftPart) and j < len(rightPart):
        if leftPart[i] <= rightPart[j]:
            A[k] = leftPart[i]
            i += 1
        else:
            A[k] = rightPart[j]
            j += 1
        k += 1

    while i < len(leftPart):
        A[k] = leftPart[i]
        i += 1
        k += 1

    while j < len(rightPart):
        A[k] = rightPart[j]
        j += 1
        k += 1

A = [2, 3, 6, 7, 11, 13, 45, 57]  
merge(A, 0, 2, 7)
print(A)  