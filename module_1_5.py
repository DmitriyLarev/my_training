immutable_var = 5, True, "String"
print(immutable_var)
# immutable_var[0] = 2 # - Если мы попытаемся изменить элемент кортежа то получим ошибку: TypeError: 'tuple' object does not support item assignment
# Элементы кортежа в Python нельзя изменять, потому что кортеж — это неизменяемый тип данных.

mutable_list = [4, 5, "apple", True]
print(mutable_list)
mutable_list.append("orange")
print(mutable_list)
