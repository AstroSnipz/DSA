def merge_sort(arr):

    if(len(arr)>1):

        left_array = arr[:len(arr)//2]
        right_array = arr[len(arr)//2:]

        print(left_array)
        print(right_array)

        # Recursive calls to sort the two halves
        merge_sort(left_array)
        merge_sort(right_array)

        # Merge the sorted halves
        i = 0  # Index for left array
        j = 0  # Index for right array
        k = 0  # Index for merged array

        while i<len(left_array) and j<len(right_array):

            if(left_array[i]<right_array[j]):
                arr[k] = left_array[i]
                i+=1
            else:
                arr[k] = right_array[j]
                j+=1
            k+=1

        # Copy any remaining elements from left_arr (if any)
        while i<len(left_array):
            arr[k] = left_array[i]
            i+=1
            k+=1

        # Copy any remaining elements from right_arr (if any)
        while j<len(left_array):
            arr[k] = right_array[j]
            j+=1
            k+=1

array = [2,3,5,1,6,8,9,4]
merge_sort(array)
print(array)