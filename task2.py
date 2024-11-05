def find_common_participants(first, second, delim = ','):
    first_group = set(first.split(delim))
    second_group = set(second.split(delim))
    return sorted(first_group.intersection(second_group))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group))
