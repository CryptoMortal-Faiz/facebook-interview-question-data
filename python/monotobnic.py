## Given an array of integers, we would like to determine whether the array is monotonic (non-decreasing/non-increasing) or not.

## https://www.geeksforgeeks.org/python-program-to-check-if-given-array-is-monotonic/ -- One solution available here

# Monotonic - 
def isMonotonic(A):
   return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
      all(A[i] >= A[i + 1] for i in range(len(A) - 1)))

# Input and Main
A = [1,2,3,4,7,8]
print(isMonotonic(A))

  
