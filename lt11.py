def rearrange(arr):
    start = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:   
            temp = arr[start]     
            arr[start] = arr[i]   
            arr[i] = temp         
  
            start += 1
    return arr

arr = [5, 1, 6, 2, 7, 4, 3]
result = rearrange(arr)
print(result)
