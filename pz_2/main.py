# Вариант 27. С начала суток прошло N секунд (N — целое). Найти количество
# секунд, прошедших с начала последнего часа.

try:
    N = int(input("Введите количество секунд: ")) 
    # Вводим количество секунд, прошедших с начала суток
    seconds_in_last_hour = N % 3600 
    # Вычисляем количество секунд, прошедших с начала последнего часа
    print("Количество секунд, прошедших с начала последнего часа:", seconds_in_last_hour)

except:
    print('N должно быть целочисленным')
