class Solution:
    def search(self, nums, target):

        lower_bound = 0
        upper_bound = len(nums) - 1

        while lower_bound <= upper_bound:
            mid = (lower_bound + upper_bound) // 2

            # Print the current state for analysis
            print(f"lower_bound: {lower_bound}, upper_bound: {upper_bound}, mid: {mid}, nums[mid]: {nums[mid]}")

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lower_bound = mid + 1
            else:
                upper_bound = mid - 1
        
        return -1

nums = [1, 3, 5, 7, 9, 11, 13, 15]
target = 9

solution = Solution()
print(solution.search(nums, target))
