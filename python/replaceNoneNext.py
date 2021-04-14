def replace_none(arr):
    if len(arr) == 0 or all(x == None for x in arr):
        return "No inp"
    for i in range(len(arr)):
        if arr[i] == None:
            arr[i] = arr[i+1]
    return arr
