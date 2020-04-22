import numpy as np
def game_core_v3(number):
    '''Делим  всегда интервал пополам. Начинаем с середины
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    pred_low = 1 # нижняя граница
    pred_high = 101  # верхняя граница (с учетом округления в меньшую сторону)
    predict = int((pred_high-pred_low)/2)
    while number != predict:
        count+=1
        if number > predict: 
            pred_low = predict
            predict = int((pred_high-pred_low)/2 + pred_low)
        elif number < predict:
            pred_high = predict
            predict = int((pred_high-pred_low)/2 + pred_low)
    return(count) # выход из цикла, если угадали
       
        
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


# Проверяем
score_game(game_core_v3)