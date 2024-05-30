def is_prime(func): # Скелет функции декоратор
    def wrapper():
        print('Простое')
        func()
    return wrapper

@is_prime # То что вызывает декоратор
def sum_three():
    total = sum(sum_three)
    print(total)

result = sum_three(2, 3, 6)
print(result)