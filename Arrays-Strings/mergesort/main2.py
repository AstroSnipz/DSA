# you can analyze the iterations here

def merge_sort(nums):
    if len(nums) > 1:
        left_array = nums[:len(nums)//2]
        right_array = nums[len(nums)//2:]

        print(f"Splitting: Left: {left_array}, Right: {right_array}")

        # Recursively sort both halves
        merge_sort(left_array)
        merge_sort(right_array)

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_array) and j < len(right_array):
            print(f"Comparing: left_array[{i}] = {left_array[i]} with right_array[{j}] = {right_array[j]} | (i={i}, j={j}, k={k})")
            if left_array[i] < right_array[j]:
                print(f"Assigning nums[{k}] = left_array[{i}] ({left_array[i]}) | (i={i}, j={j}, k={k})")
                nums[k] = left_array[i]
                i += 1
            else:
                print(f"Assigning nums[{k}] = right_array[{j}] ({right_array[j]}) | (i={i}, j={j}, k={k})")
                nums[k] = right_array[j]
                j += 1
            k += 1
            print(f"Resulting nums after merging: {nums}")
            print()

        # Copy any remaining elements from left_array
        while i < len(left_array):
            print(f"Remaining left_array[{i}] = {left_array[i]}, assigning to nums[{k}] | (i={i}, k={k})")
            nums[k] = left_array[i]
            i += 1
            k += 1
            print(f"Resulting nums after merging: {nums}")
            print()

        # Copy any remaining elements from right_array
        while j < len(right_array):
            print(f"Remaining right_array[{j}] = {right_array[j]}, assigning to nums[{k}] | (j={j}, k={k})")
            nums[k] = right_array[j]
            j += 1
            k += 1
            print(f"Resulting nums after merging: {nums}")
            print()

# Example list
nums = [2, 6, 1, 7, 8, 4, 7, 3]
merge_sort(nums)
print("Sorted array:", nums)
