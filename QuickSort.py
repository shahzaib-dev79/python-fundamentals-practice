def quick_sort(nums):
    if len(nums) <= 1:
        return nums

    pivot = nums[len(nums) // 2]
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# --- Example usage ---
print(quick_sort([5, 2, 9, 1, 5, 6]))
print(quick_sort([]))
print(quick_sort([3]))
print(quick_sort([9, 8, 7, 6, 5]))