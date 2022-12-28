def check_for_negative(arr):
    index = []
    for i in range(len(arr)):
        if arr[i] in ('+', '-'):
            if arr[i-1] == '(' and arr[i+1] == '(':
                index.append(i)

    return index
