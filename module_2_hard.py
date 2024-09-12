field = int(input("Введите число: "))
list_num = []
result = ""

for i in range(1, 21):
    for j in range(1, 21):
        if field % (i + j) == 0 and i < j:
            num_pair = [i, j]
            for k in num_pair:
                list_num.extend(num_pair)
                break

for el in list_num:
    result += str(el)
    
if 3 <= field <= 20:
    print(f"Пароль: {result}")
else:
    print("Неверное число!")
