# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
#   A, E, I, O, U, L, N, S, T, R – 1 очко;
#   D, G – 2 очка;
#   B, C, M, P – 3 очка;
#   F, H, V, W, Y – 4 очка;
#   K – 5 очков;
#   J, X – 8 очков;
#   Q, Z – 10 очков.
# А русские буквы оцениваются так:
#   А, В, Е, И, Н, О, Р, С, Т – 1 очко;
#   Д, К, Л, М, П, У – 2 очка;
#   Б, Г, Ё, Ь, Я – 3 очка;
#   Й, Ы – 4 очка;
#   Ж, З, Х, Ц, Ч – 5 очков;
#   Ш, Э, Ю – 8 очков;
#   Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

#
# *Пример:*
#
# ноутбук
#     12


letter_to_score_english = {
    **dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'], 1),
    **dict.fromkeys(['D', 'G'], 2),
    **dict.fromkeys(['B', 'C', 'M', 'P'], 3),
    **dict.fromkeys(['F', 'H', 'V', 'W', 'Y'], 4),
    'K': 5,
    **dict.fromkeys(['J', 'X'], 8),
    **dict.fromkeys(['Q', 'Z'], 10)
}

letter_to_score_russian = {
    **dict.fromkeys(['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 1),
    **dict.fromkeys(['Д', 'К', 'Л', 'М', 'П', 'У'], 2),
    **dict.fromkeys(['Б', 'Г', 'Ё', 'Ь', 'Я'], 3),
    'Й': 4,
    'Ы': 4,
    **dict.fromkeys(['Ж', 'З', 'Х', 'Ц', 'Ч'], 5),
    **dict.fromkeys(['Ш', 'Э', 'Ю'], 8),
    **dict.fromkeys(['Ф', 'Щ', 'Ъ'], 10)
}

input_word = input('Введите слово: ')
score = 0
for c in input_word:
    character = c.upper()
    if character in letter_to_score_english:
        score += letter_to_score_english.get(character)
    elif character in letter_to_score_russian:
        score += letter_to_score_russian.get(character)
print(f'Вы набрали: {score} очков')
