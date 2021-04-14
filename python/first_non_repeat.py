## Non repeating element in the array

def firstNonRepeating(arr, n):
  
    for i in range(n):
        j = 0
        while(j < n):
            if (i != j and arr[i] == arr[j]):
                break
            j += 1
        if (j == n):
            return arr[i]
      
    return -1
      
# Driver code
arr = [ 9, 4, 9, 6, 7, 4 ]
n = len(arr)
print(firstNonRepeating(arr, n))
