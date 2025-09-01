def removeduplicates(arr):
    start=1

    for i in range(2,len(arr)):
        if arr[i]!=arr[start-1]:
            start+=1
            arr[start]=arr[i]

    return start+1

arr=[3,3,5,7,7,7,7,9,9,9,12,12]
size=removeduplicates(arr)
print(size)