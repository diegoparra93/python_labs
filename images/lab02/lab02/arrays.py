def min_max(a):
    if not a:
        return 'ValueError'
    max_ = -10 ** 10
    min_ = 10 ** 10
    for i in a:
        if i > max_:
            max_ = i
        if i < min_:
            min_ = i
    return (min_, max_)

# Ahora probamos
print("Test 1:", min_max([3, -1, 5, 5, 0]))
print("Test 2:", min_max([42]))
print("Test 3:", min_max([]))