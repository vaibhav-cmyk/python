# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

nums= [2,7,11,15]
target = 13

class Solution:
    def twoSum(self,nums,target):
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
                
            
sum=Solution()
result=sum.twoSum(nums,target)
print(result)




