## Sum of two elements in Array is equal to given sum

def two_sum(arr,target):
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)):
            if arr[i] + arr[j] == target:
                return [arr[i],arr[j]]


print(two_sum([2,3,4,5],9))
