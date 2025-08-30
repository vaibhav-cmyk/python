# low = 1
# high = 5

# count = 0
# for i in range(low, high+1):   # include 'high'
#     if i % 2 != 0:             # odd check
#         print(i)
#         count += 1

# print("Total odd numbers =", count)


low =1
high = 5
count =0
ans=[]
for i in range(low,high+1):
    ans.append(i)
    # print(i, end="")
    
for i in ans:
    if i%2!=0:
        count+=1
       
    
print("count is",count)
