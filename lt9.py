nums=[1,2,3,4] #output[1,3,6,10]

sum=[]
sum.append(nums[0])
for i in range(1,len(nums)):
    x=sum[i-1]+nums[i]
    sum.append(x)

print(sum)
    

