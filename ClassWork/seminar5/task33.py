# 33. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
import random

count_of_scores = int(input('Введите количество оценок: '))
scores_list = [random.randint(1, 5) for _ in range(count_of_scores)]
print(f'Before: {scores_list}')
minimal_score = min(scores_list)
maximum_score = max(scores_list)
for i in range(len(scores_list)):
    if scores_list[i] == maximum_score:
        scores_list[i] = minimal_score
print(f'After: {scores_list}')
