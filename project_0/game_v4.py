"""Игра угадай число
Компьютер угадывает число с учтотом больше или меньше загаданного
"""

import numpy as np


def mind_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    predict = 50 # перове значение поиска 
    count = 0 # обнуление счетчика
    down = 1 # нижняя граница
    up = 101 # верхняя граница
    while predict != number:
        count+=1
        if predict > number:
            up = predict # отсекаем все что выше границ поиска
        else:
            down=predict # отсекам все что ниже границ поиска
        predict = down + (up - down) // 2 # ищем середину оставщегося ряда чисел
    return count


def score_game(mind_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(mind_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(mind_predict)
