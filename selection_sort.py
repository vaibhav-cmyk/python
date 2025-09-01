# class Selection_Sort:
#     def selectionSort(self, num):
#         n = len(num)

#         for i in range(n):
#             smallIndex = i  
#             for j in range(i + 1, n):
#                 if num[j] < num[smallIndex]:
#                     smallIndex = j
#             # swap after finding the smallest
#             temp = num[i]
#             num[i] = num[smallIndex]
#             num[smallIndex] = temp

#         return num


# num = [4, 1, 5, 2, 3]
# result = Selection_Sort()
# result1 = result.selectionSort(num)
# print(result1)





class Solution:
    def sort_asc(self,arr):
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]>arr[j]:
                    temp=arr[i]
                    arr[i]=arr[j]
                    arr[j]=temp
        return arr            
arr = [87, 12, 45, 99, 23, 56, 11, 72, 34, 67, 
       5, 88, 29, 61, 18, 90, 44, 2, 76, 39, 
       100, 9, 53, 70, 31, 14, 81, 27, 95, 48, 
       6, 63, 21, 36, 78]

num=Solution()
num1=num.sort_asc(arr)
print(num1)