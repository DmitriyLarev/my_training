import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        day = 0
        while enemies:
            enemies -= self.power
            day += 1
            time.sleep(1)
            print(f"{self.name} сражается {day} день(дня)..., осталось {enemies} воинов")
        print(f"{self.name} одержал победу спустя {day} дней(дня)!")


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()

