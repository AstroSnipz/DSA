#brute force method
def largeSubArray(nums, target):

    start_index = 0
    end_index = 0
    max_sum = 0
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            print(j)
            current_sum+=nums[j]
            if(current_sum<=target and current_sum>=max_sum):
                max_sum=current_sum
                start_index, end_index = i,j
    return start_index, end_index





# Test the function
nums = [2, 5, 1, 7, 10]
target = 14
s, e = largeSubArray(nums, target)
print(nums[s:e+1])
