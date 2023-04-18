# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
s = input('Введите строку: ')
list_of_chars = list(s)
letter_to_count = dict()
for c in list_of_chars:
    if c in letter_to_count:
        letter_to_count[c] = letter_to_count[c] + 1
    else:
        letter_to_count[c] = 1
    count_of_repeats = letter_to_count[c] - 1
    print(f"{c}_{count_of_repeats}" if count_of_repeats > 0 else c, end=' ')
