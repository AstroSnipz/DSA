def binary_search(target, nums):

    lower_bound = 0 
    upper_bound = len(nums)-1

    while lower_bound<=upper_bound:
        mid = (lower_bound+upper_bound)//2

        if(nums[mid]==target):
            return mid
        elif(nums[mid]<target):
            lower_bound = mid+1
        else:
            upper_bound = mid-1
    return -1

target = 5
nums = [1,3,5,6,7,9,10,12,14,15,116,224]
print(binary_search(target, nums))