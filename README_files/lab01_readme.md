### Задание 1
```
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
```
![Photo 1]()
