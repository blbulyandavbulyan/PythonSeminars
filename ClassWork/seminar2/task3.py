'''
Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы.
Их интересует, сколько дней длилась самая длинная оттепель.
Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия.
Напишите программу, помогающую синоптикам в работе.
'''
import random
count_of_days_with_positive_temperature = 0
for i in range(31):
    current_temperature = random.randint(-3, 3)
    print(current_temperature)
    if(current_temperature > 0):
        count_of_days_with_positive_temperature+=1
    else:
        count_of_days_with_positive_temperature = 0
print(count_of_days_with_positive_temperature)