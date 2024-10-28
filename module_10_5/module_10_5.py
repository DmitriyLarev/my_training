import multiprocessing
import time
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# # Линейный вызов
# start = time.time()
# for file in filenames:
#     read_info(file)
# finish = time.time()
# elapsed = datetime.timedelta(seconds=finish - start)
# print(elapsed) # Вывод в консоле: ~0:00:06.136587

# Многопроцессный
if __name__ == '__main__':
    start = time.time()
    with multiprocessing.Pool(len(filenames)) as pool:
        pool.map(read_info, filenames)
    finish = time.time()
    elapsed = datetime.timedelta(seconds=finish - start)
    print(elapsed)
