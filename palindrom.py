## Задача на палиндромы
def solve(phrases: list):
    result = [] 
    for phrase in phrases:
        phrase_word = phrase.replace(' ', '')
        if phrase_word == phrase_word[::-1]:
           result.append(phrase)
    return result

if __name__ == '__main__':
    
    phrases = ["нажал кабан на баклажан", "дом как комод", "рвал дед лавр", "азот калий и лактоза",
               "а собака боса", "тонет енот", "карман мрак", "пуст суп"]
    result = solve(phrases)
    assert result == ["нажал кабан на баклажан", "рвал дед лавр", "азот калий и лактоза",
               "а собака боса", "тонет енот", "пуст суп"], f"Неверный результат: {result}"
    print(f"Палиндромы: {result}")

    ## Задача 2
    def solve(todo_list: list, workday: float = 8):
    worktime = 0.0
    for time in todo_list: # посчитайте в цикле сумму рабочего времени и сохраните в переменную worktime
        worktime += time[1]
    return workday - worktime