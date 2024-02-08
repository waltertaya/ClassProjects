def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    
    # Merge the two halves by comparing elements
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Add remaining elements from the left half
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    
    # Add remaining elements from the right half
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    
    return merged

# Example usage
arr = [3, 1, 7, 2, 6, 4, 5]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
