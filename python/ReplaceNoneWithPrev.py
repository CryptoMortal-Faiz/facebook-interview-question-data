def replace_none(arr):
    if len(arr) == 0 or all(x == None for x in arr):
        return "No inp"
    for i in range(len(arr)):
        if arr[i] == None:
            arr[i] = arr[i-1]
    return arr

    
a1 = [None,1,2,None,None,3,None]
a2 = [None]
a3 = [1,2,3,4,5]
a4 = [None,0,None]
a5 = [0,0,0,0,0]
a6 = [None, None, None]

print(replace_none(a1))
print(replace_none(a2))
print(replace_none(a3))
print(replace_none(a4))
print(replace_none(a5))
print(replace_none(a6))
