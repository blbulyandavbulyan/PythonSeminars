'''
Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
'''
import random
count_of_watermelon = int(input('Введите количество арбузов: '))
minimum_weight = 30000
maximum_weight = 1
for i in range(count_of_watermelon):
    weight_of_watermelon = random.randint(1, 25000)
    print(f'Вес арбуза {i+1}: {weight_of_watermelon}')
    if weight_of_watermelon > maximum_weight:
        maximum_weight = weight_of_watermelon
    if weight_of_watermelon < minimum_weight:
        minimum_weight = weight_of_watermelon
print(f'Для себя: {maximum_weight}\nДля тёщи: {minimum_weight}')
