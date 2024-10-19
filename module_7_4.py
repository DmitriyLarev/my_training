team1 = "Мастера кода"
team2 = "Волшебники данных"
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = "Победа команды %s!" % team1
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = "Победа команды {}!".format(team2)
else:
    result = "Ничья!"

challenge_result = result

# %
print("В команде %s участников: %d ! " % (team1, team1_num))
print("Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num))

# .format()
print("Команда {} решила задач: {} !".format(team2, score_2))
print("{} решили задачи за {} с !".format(team2, team2_time))

# f-string
print(f"Команды решили {score_1} и {score_2} задач.")
print(f"Результат битвы: {challenge_result}")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")