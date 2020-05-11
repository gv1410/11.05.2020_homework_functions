
def calc_funktion(weight, height):
    calc_funktion_result = int(weight / ((height / 100)**2))
    return calc_funktion_result

def user_name_input():
    user_name = input('Введите ваше имя: ')
    return user_name

def user_input():
    
    user_sex = input('Введите ваш пол(м/ж): ')
    user_age = int(input('Введите ваш возраст(от 18 до 40): '))
    user_weight = float(input('Введите свой вес (кг): '))
    user_height = float(input('Введите свой рост (см): '))




    calc_result = calc_funktion(user_weight, user_height)
            
        
    database = [calc_result, user_weight, user_height, user_sex, user_age]
    return database

def stop_cycle():
    question = input('Ввести еще данные?(да/нет ): ')
    return question

def user_data_print(request, data_calc_result):

    print('\n Индекс массы тела ' + request + ' равен: ', data_calc_result)

def user_calc_result_print(data_calc_result):
    print('20' + ('=' * (data_calc_result - 20)) + '|' + \
    ('=' * (50 - data_calc_result)) + '50')

def user_recommendations(data_calc_result, data_sex, data_age):
    if data_calc_result < 20 and data_sex == 'м' and 18 <= data_age >= 40:
        print('Для мужчин в возрасте от 18 до 40 это очень мало!')
    elif 20 <= data_calc_result <=25 and data_sex == 'м' and 18 <= data_age <= 40:
        print('Для мужчин в возрасте от 18 до 40 это норма!')
    elif 25 < data_calc_result <=30 and data_sex == 'м' and 18 <= data_age <= 40:
        print('Для мужчин в возрасте от 18 до 40 это состояние предожирения!')
    elif 30 < data_calc_result <=35 and data_sex == 'м' and 18 <= data_age <= 40:
        print('Для мужчин в возрасте от 18 до 40 это ожирение первой степени!')
    elif 35 < data_calc_result <=40 and data_sex == 'м' and 18 <= data_age <= 40:
        print('Для мужчин в возрасте от 18 до 40 это ожирение второй степени!')
    elif 40 < data_calc_result and data_sex == 'м' and 18 <= data_age <= 40:
        print('Для мужчин в возрасте от 18 до 40 это ожирение третей степени!')
    elif data_calc_result < 20 and data_sex == 'ж' and 18 <= data_age >= 40:
        print('Для женщин в возрасте от 18 до 40 это очень мало!')
    elif 20 <= data_calc_result <=25 and data_sex == 'ж' and 18 <= data_age <= 40:
        print('Для женщин в возрасте от 18 до 40 это норма!')
    elif 25 < data_calc_result <=30 and data_sex == 'ж' and 18 <= data_age <= 40:
        print('Для женщин в возрасте от 18 до 40 это состояние предожирения!')
    elif 30 < data_calc_result <=35 and data_sex == 'ж' and 18 <= data_age <= 40:
        print('Для женщин в возрасте от 18 до 40 это ожирение первой степени!')
    elif 35 < data_calc_result <=40 and data_sex == 'ж' and 18 <= data_age <= 40:
        print('Для женщин в возрасте от 18 до 40 это ожирение второй степени!')
    elif 40 < data_calc_result and data_sex == 'ж' and 18 <= data_age <= 40:
        print('Для женщин в возрасте от 18 до 40 это ожирение третей степени!')
    else:
        print('Что бы получить рекомендацию введите другие данные!!!')

def main():
    user_database = {}
    cycle = True



    while cycle:
        user_name_input_result = user_name_input()
        user_input_result = user_input()

    
        user_database[user_name_input_result] = user_input_result

        stop_cycle_input = stop_cycle()

        if stop_cycle_input == 'да':
            cycle = True
        elif stop_cycle_input == 'нет':
            cycle = False
    
    user_request = input('Чьи данные вывести на экран?' + str(user_database.keys()) + ': ')

    user_data = user_database[user_request]




    user_data_calc_result = int(user_data[0])

    user_data_weight = int(user_data[1])

    user_data_height = int(user_data[2])

    user_data_sex = str(user_data[3])

    user_data_age = int(user_data[4])



    user_data_print(user_request, user_data_calc_result)
    user_calc_result_print(user_data_calc_result)



    user_recommendations(user_data_calc_result, user_data_sex, user_data_age)

if __name__ == "__main__":
    main()

