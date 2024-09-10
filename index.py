def bead_sort(arr):
     if any(not isinstance(x, int) or x < 0 for x in arr):
          raise TypeError("Error")
          
     for _ in range(0, len(arr)):
          for i, (upper, lower) in enumerate(zip(arr , arr[1:])):
               if upper > lower:
                    arr[i] -= upper - lower
                    arr[i+1] += upper - lower
     return arr
               
print(bead_sort([1,6,7,3]))