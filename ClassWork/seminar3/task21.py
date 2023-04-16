
#21. Напишите программу для печати всех уникальных значений в словаре.
list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII ":"S007"}]
unique_values = set()
for dicts in list_1:
    for value in dicts.values():
        unique_values.add(value)
print(unique_values)