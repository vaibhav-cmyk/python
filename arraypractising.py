# 🟣 Patterns & Others
# 1️⃣8️⃣ Find the difference between the largest and smallest element.
# 1️⃣9️⃣ Check if the array is sorted (ascending or descending).

# 🚀 Challenge Problems
# ✨ Rotate the array to the right by k steps.
# ✨ Find the pair of elements that sum to a given number.
# ✨ Find the frequency of each unique element in the array.
# ✨ Remove all occurrences of a specific element from the array.
# ✨ Find the element which occurs the most number of times.




# import array as arr 
# num = arr.array('i',[100,32,13,56,22,88,444,44])
# sorted_array = arr.array('i',sorted(num))
# print('sorted array',sorted_array)

# # print('smallest value is:',sorted_array[0])
# smallest = sorted_array[0]
# print(smallest)

# # print('largets values is:',sorted_array[-1])
# largest = sorted_array[-1]
# print(largest)

# result = largest - smallest
# print('result is:',result)

# import array as arr
# num = arr.array('i',[1,2,3,4,8,5])
# ascending = True
# for i in range(len(num)-1):
#     if num[i] > num[i+1]:
#         ascending =  False
#         break
# if ascending:
#     print("array is ascending")
# else:
#     print("array is descending")
    
   # 2️⃣0️⃣ Split the array into two halves and print both halves.
# import array as arr
# import math as math
# num = arr.array('i',[1,2,3,4,5,6,7,8,9,10])

# start_index = num[0]

# end_index = num[-1]

# # print(start_index)
# # print(end_index)

# half = int((start_index + end_index)/2)
# # print(half)
# print('fst half')
# for i in range(half):
#     print(num[i])

# print('second half')
# for j in range(half,len(num)):
#     print(num[j])

# import array as arr
# dig = arr.array('i',[1,2,3,4,5,6])

# key  = int(input('enter key:'))
# key = key % len(dig)

# rotated = dig[-key:]+dig[:-key]

# rotated_array = arr.array('i',rotated)
# print(rotated_array)


# x = "4" + "2"
# val = int(x) + 6
# print(val)
# print(float(val))




import pandas as pd

# Create a dictionary with categories and example formulas
data = {
    "Category": [
        "Lookup", "Lookup", "Conditional", "Aggregate", "Text", "Date", "Dynamic Arrays"
    ],
    "Formula Template": [
        '=XLOOKUP(B2, Customers[ID], Customers[Name])',
        '=INDEX(A2:A10, MATCH(105, B2:B10, 0))',
        '=IF(D2>1000, "High", "Low")',
        '=SUMIFS(Sales[Amount], Sales[Region], G2)',
        '=TEXTJOIN(", ", TRUE, A2:C2)',
        '=NETWORKDAYS(A2, B2, Holidays!A:A)',
        '=UNIQUE(FILTER(Orders[Product], Orders[Region]="East"))'
    ],
    "Usage Description": [
        "Fetch customer name based on ID",
        "Flexible lookup using index and match",
        "Categorize revenue",
        "Sum sales filtered by region",
        "Combine multiple fields with comma",
        "Calculate business days between dates",
        "List unique products for East region"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel("Excel_Formulas_for_Data_Analytics.xlsx", index=False)
