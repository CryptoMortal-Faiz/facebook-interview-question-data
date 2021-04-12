# Return all the idices of the target element in the array

def get_index(arr,target):
    n = len(arr)
    if n == 0 or all(x==None for x in arr):
        return "Empty array"
    elif target not in arr:
        return [-1,-1]
    res = []
    for i in range(0,len(arr)-1):
        if arr[i] == target:
            res.append(i)
    return res
        
    
## Driver code    
a1 = [1,0,0,-9,0,0,9,0]
a2 = []
a3 = [None,None]
print(get_index(a1,9))
print(get_index(a2,9))
print(get_index(a3,9))
print(get_index(a1,6))

'''
[6]
Empty array
Empty array
[-1, -1]
'''
