from typing import Counter
import numpy as np
from numpy import random
def predict_with_limits(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попытокarrow_up в readme
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    limit_a =  1 # нижняя граница
    count = 0 # обнуление счетчика
    limit_b = 101 # верхняя граница
    predict = np.random.randint(limit_a, limit_b) # задаем первое рандомное число 
    
    while number != predict:
        count += 1
        if number > predict: # если загданное больше предложенного
            predict += 1 # увеличиваем предложенное на 1
            limit_b = number # устанавливаем верхнюю границу как загаданное

        elif number < predict: # если загданное больше предложенного
            predict -= 1 # уменьшаем предложенное на 1
            limit_a = number # устанавливаем нижнюю границу как загаданное

    return count
def score_game(predict_with_limits) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        predict_with_limits ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(predict_with_limits(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(predict_with_limits)