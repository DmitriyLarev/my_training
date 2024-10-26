def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result % 2 == 0:
            print('Составное')
        else:
            print('Простое')
        return result

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
result = sum_three(3, 3, 6)
print(result)
