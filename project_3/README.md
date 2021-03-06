# Проект 3. Проверка отзывов отелей Booking.com

## Оглавление  
[1. Описание проекта]
[2. Какой кейс решаем?]
[3. Краткая информация о данных]
[4. Этапы работы над проектом] 
[5. Результат]   
[6. Выводы]
[7. Воспроизводимость]

### Описание проекта    
Мы работаем датасаентистом в компании Booking. Одна из проблем компании — это нечестные отели, которые накручивают себе рейтинг. Одним из способов нахождения таких отелей является построение модели, которая предсказывает рейтинг отеля. Если предсказания модели сильно отличаются от фактического результата, то, возможно, отель играет нечестно, и его стоит проверить.

### Какой кейс решаем?    
Необходимо создать и обучить модель для предсказания рейтинга отлей на основе имеющихся данных.

**Условия соревнования:**  
Данное соревнование является бессрочным и доступно для всех потоков.
Срок выполнения соревнования устанавливается индивидуально в каждом потоке.
Тестовая выборка представлена в LeaderBoard целиком.
Делаем реальный ML продукт, который потом сможет нормально работать на новых данных.

**Метрика качества**     
Метрика качества
Результаты оцениваются по метрике MAPE

Файл представления
Для каждого id отеля в наборе тестовых данных вы должны предсказать рейтинг отеля для reviewer_score переменной. Файл должен содержать заголовок и иметь следующий формат:


### Краткая информация о данных

Данные для соревнования
hotels_train.csv - набор данных для обучения (ссылка для скачивания: https://drive.google.com/file/d/19pSXLj2gpJ_JoPmKsl84XIoO9A9DlH7I/view?usp=sharing)
hotels_test.csv - набор данных для оценки качества (ссылка для скачивания: https://drive.google.com/file/d/19waIsFkyCpBDsqSPlwVxPRBKLF_A2S_c/view?usp=sharing)
submission.csv - файл сабмишна в нужном формате (ссылка для скачивания: https://drive.google.com/file/d/19oXE7IKCrBbLsNHBfVnBeXdNCToNAOU7/view?usp=sharing)

Признаки
hotel_address - адрес отеля
review_date - дата, когда рецензент разместил соответствующий отзыв.
average_score - средний балл отеля, рассчитанный на основе последнего комментария за последний год
hotel_name - название отеля
reviewer_nationality - национальность рецензента
negative_review - отрицательный отзыв, который рецензент дал отелю.
review_total_negative_word_counts - общее количество слов в отрицательном отзыв
positive_review - положительный отзыв, который рецензент дал отелю
review_total_positive_word_counts - общее количество слов в положительном отзыве
reviewer_score - оценка, которую рецензент поставил отелю на основе своего опыта
total_number_of_reviews_reviewer_has_given - количество отзывов, которые рецензенты дали в прошлом
total_number_of_reviews - общее количество действительных отзывов об отеле
tags - теги, которые рецензент дал отелю.
days_since_review - продолжительность между датой проверки и датой очистки
additional_number_of_scoring - есть также некоторые гости, которые просто поставили оценку сервису, а не оставили отзыв. Это число указывает, сколько там действительных оценок без проверки.
lat - широта отеля
lng - долгота отеля

### Этапы работы над проектом  
 0 Загружаем данные дял соревнования
 1 Очистка данных
 2 Проектирование признаков
 3 Отбор признаков
 4 Подготовка данных дял модели
 5 Созадем и обучаем модель

### Результаты:  

Получен MAPE: 12.49
Сформирован файл submission_last.csv содержащий оценки отелям спрогнозированные моделью. 

### Выводы:  

Метрика МАРЕ улучшена с базовых 14% до 12,49%
Возможно использование модели для дальнейшей оценки адекватности оценок отелей.

### Воспроизводимость:  
Использованная конфигурция окружения:

 *Через pip:*

pip install -r [requirements.txt]