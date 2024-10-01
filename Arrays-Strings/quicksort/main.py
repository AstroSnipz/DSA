def sorting(nums):

    if len(nums) <= 1:
        return nums

    swapedNum, current_i = swap(nums)
    left, right = partition(swapedNum, current_i)

    left_sorted = sorting(left)
    right_sorted = sorting(right)

    return left_sorted + [swapedNum[current_i]] + right_sorted


def swap(nums):

    pivot = nums[-1]
    i = -1

    for j in range(len(nums)):
        if nums[j] <= pivot:
            i+=1
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
    
    return nums, i

def partition(nums, i):
    mid = nums[i]
    left = nums[:i]
    right = nums[i+1:]

    return left, right

nums = [2,3,3,34,2,4,4556,2,1,32,54,7,476,3,325,1,1,5,6,7,7,9,8,7,6,5,4,3,2,21,1,1,11111,11]
print(sorting(nums))