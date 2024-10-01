class Solution:
    def twoSum(self, nums, target):

        for i in range(len(nums)):
            p = 1
            if(nums[i]+nums[p] == target):
                return [i, p]
            p+=1

    