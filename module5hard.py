from time import sleep

class User:
    """
    Класс пользователя,  содержит никнейм, пароль, возраст
    """
    nickname = None
    password = None
    age = 0

    def __init__(self, nickname = nickname, password =  password, age = age):
       self.nickname = nickname
       self.password = password
       self.age = age

    def user_list(self):
        return [self.nickname, self.password, self.age]

user_obj = User()

class Video:
    """
    Класс видео, содержит заголовок(название) видео, длительность, время остановки(сек), ограничение по возрасту
    """
    title = None
    duration = None
    time_now = 0
    adult_mode = False

    def __init__(self, title = title, duration = duration, time_now = time_now, adult_mode = adult_mode):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def video_list(self):
        return [self.title, self.duration, self.time_now, self.adult_mode]

video_obj = Video()

class UrTube:
    """
    Класс UrTube, содержит список объектов пользователей, список объеков видео, текущий пользователь
    """
    def __init__(self):
        self.users = [user_obj.user_list()]
        self.videos = [video_obj.video_list()]
        self.current_user = None
        self.current_user_age = 0

    def log_in(self, nickname, password):
        for i in self.users:
            if nickname in i:
                if hash(password) in i:
                    self.current_user = i[0]
                    self.current_user_age = i[2]
                    break

    def register(self,nickname, password, age):
        exists = False
        for i in self.users:
            if nickname not in i:
                exists = True
            else:
                exists = False
                break
        if exists:
            self.users.append([nickname, hash(password), age])
            self.log_in(nickname, password)
        else:
            print(f"Пользователь {nickname} уже существует")

    def log_out(self):
        self.current_user = None

    def add(self, *objects):
        for i in objects:
            self.videos.append(i.video_list())

    def get_videos(self, search_word):
        list_of_videos = []
        for i in self.videos:
            if search_word.lower() in str(i[0]).lower():
                list_of_videos.append(i[0])
        return list_of_videos

    def watch_video(self, film_name):
        if self.current_user:
            for i in self.videos:
                if film_name == i[0]:
                    if i[3]:
                        if self.current_user_age >= 18:
                            j = 1
                            while j != i[1] + 1:
                                print(j, end=" ")
                                sleep(1)
                                j += 1
                            i[2] = 0
                            print("Конец видео")
                            break
                        else:
                            print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    else:
                        j = 1
                        while j != i[1] + 1:
                            print(j, end=" ")
                            sleep(1)
                            j += 1
                        i[2] = 0
                        print("Конец видео")
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')