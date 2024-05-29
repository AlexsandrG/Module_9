def is_odd(x):
    return x ** 2


def filter_1(x):
    return x % 2


my_numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

results = map(is_odd, filter(filter_1, my_numbers))
print(list(results))
