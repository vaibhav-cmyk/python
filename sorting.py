#for ascending


class Sorting:
    def Bubble_Sort(self,num):
        n=len(num)
        for i in range(n):
            for j in range(n-i-1):
                if num[j]>num[j+1]:
                    #swp
                    temp=num[j]
                    num[j]=num[j+1]
                    num[j+1]=temp
                    
        return num
    
    def selectionSort(self, num):
        n = len(num)

        for i in range(n):
            smallIndex = i  
            for j in range(i + 1, n):
                if num[j] < num[smallIndex]:
                    smallIndex = j
            # swap after finding the smallest
            temp = num[i]
            num[i] = num[smallIndex]
            num[smallIndex] = temp

        return num


num = [9, 3, 7, 1, 8, 4, 2, 6, 5]
result=Sorting()
print("Bubble Sort:")
result1=result.Bubble_Sort(num)
print(result1)
print('\n')
print("SelectionSort:")
result1=result.selectionSort(num)
print(result1)


#time complexity=O(n^2)


#for descending

# class Sorting:
#     def Bubble_Sort(self,num):
#         n=len(num)
#         isSwap=False
#         for i in range(n):
#             for j in range(n-i-1):
#                 if num[j]>num[j+1]:
#                     j+=1
#                 else:
#                     temp=num[j]
#                     num[j]=num[j+1]
#                     num[j+1]=temp
                    
#         return num

# num = [3, 9, 7, 1, 8, 4, 2, 6, 5]
# result=Sorting()
# result1=result.Bubble_Sort(num)
# print(result1)
