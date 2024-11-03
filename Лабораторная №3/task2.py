# TODO Напишите функцию find_common_participants
def find_common_participants(str_1, str_2, n=','):
    group_1 = str_1.split(n)
    group_2 = str_2.split(n)

    common = sorted(set(group_1) & set(group_2))
    return common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group, participants_second_group, '|')
print(common_participants)
