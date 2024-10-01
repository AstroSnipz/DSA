# sliding window (constant window)

# Function to find the maximum sum of any subarray of length `k` using the sliding window technique
def maxSubArray(nums, k):

    # If the length of nums is less than k, return 0 (no valid subarray possible)
    if len(nums) < k:
        return 0

    # Calculate the initial sum of the first `k` elements in the array
    total = sum(nums[:k])
    # Set max_sum to the initial sum of the first window
    max_sum = total

    # Loop through the array to slide the window from the start index 0 up to `len(nums) - k`.
    # This loop helps us iterate through the array and slide the window across its elements.
    # The purpose is to traverse all possible windows of size `k` and compute the sum of each window using the sliding window approach.
    #
    # Why `len(nums) - k`?
    # - `len(nums) - k` is the number of times we need to slide the window across the `nums` list.
    # - When `k` is subtracted from `len(nums)`, it tells us how many windows we can slide through:
    #     - For example, if `nums` has 10 elements and `k = 3`, then `len(nums) - k` would be `10 - 3 = 7`.
    #     - This means we can have 7 different windows of size `k = 3`, starting from index `0` up to index `6`.
    # - We stop sliding the window when we reach `len(nums) - k` to ensure the window size remains `k` and we don't go out of bounds.
    for i in range(len(nums) - k):
        # Subtract the element that is sliding out of the window (at index `i`)
        total -= nums[i]
        # Add the new element that is sliding into the window (at index `i + k`)
        total += nums[i + k]

        # Update max_sum if the current window's sum is greater than max_sum
        max_sum = max(max_sum, total)

    # Return the maximum sum of any subarray of length `k`
    return max_sum

# Test case: find the maximum sum of any subarray of length 4 in the given list
nums = [-1, 2, 3, 3, 4, 5, -1]
k = 4

# Output should be 15 because the subarray [3, 3, 4, 5] has the maximum sum of 15
print(maxSubArray(nums, k))
