# распределение игроков между собой
import random


def random_assignment(user_ids):
    # Создаем копию списка user_ids
    shuffled_ids = user_ids.copy()

    # Перемешиваем элементы списка случайным образом
    random.shuffle(shuffled_ids)

    # Формируем пары (id, assigned_id)
    assignments = list(zip(user_ids, shuffled_ids))

    return assignments
