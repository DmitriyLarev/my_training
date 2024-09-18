def get_multiplied_digits(number):
    str_number = str(int(number))
    first = int(str_number[0])
    if str_number[-1] == "0":
        str_number = str_number[:-1]
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(40203)
print(result)
result = get_multiplied_digits(7)
print(result)
result = get_multiplied_digits(240)
print(result)
result = get_multiplied_digits(240450)
print(result)
