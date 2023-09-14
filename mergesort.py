import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array in half
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
    left_idx, right_idx = 0, 0

    # Merge the two halves while they have elements
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    # Append any remaining elements (if any)
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    
    return merged

# Generate a random list of 1000 integers between 1 and 10,000
random_list = [random.randint(1, 10000) for _ in range(1000)]

# Sort the list using the merge sort algorithm
sorted_list = merge_sort(random_list)

# Print the first few elements of the sorted list to verify
print("Sorted list:", sorted_list)
