def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        for i in range(2, result):
            if result % i == 0:
                return f'{result} \n Составное'
            else:
                return f' {result} \n Простое'
    return wrapper


@is_prime
def sum_three(*args):
    total = 0
    for number in args:
        total += number
    return total


result = sum_three(2, 3, 6)
print(result)