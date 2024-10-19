import os
import time

for root, dirs, files in os.walk("."):
    for file in files:
        filepath = os.path.join("module_7_5.py")
        filetime = os.path.getmtime("module_7_5.py")
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize("module_7_5.py")
        parent_dir = os.path.dirname(r"C:\Users\Дмитрий\PycharmProjects\my_training\module_7_5\module_7_5.py")
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

