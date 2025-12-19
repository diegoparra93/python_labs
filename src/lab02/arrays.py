def min_max(nums):
    if not nums:
        return ValueError

    max_val = nums[0]
    min_val = nums[0]

    for num in nums:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return (min_val, max_val)


def unique_sorted(nums):
    return sorted(set(nums))


def flatten(mat):
    if not mat:
        return []

    result = []

    for item in mat:
        if not isinstance(item, (list, tuple)):
            return TypeError
        result.extend(item)

    return result


print("min_max")

print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))

print("unique_sorted")

print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

print("flatten")

print(flatten([[1, 2], [3, 4]]))
print(flatten(([1, 2], (3, 4, 5))))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
