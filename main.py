def sum_digits(number):
    number_str = str(number)
    q = 0
    for digit in number_str:
        q += int(digit)
    return q
while True:
    try:
        number = int(input("введите число: "))
        if number < 0:
            print("Ошибка: введено отрицательное число")
        else:
            digit_sum = sum_digits(number)
            print("результат: ", digit_sum)
    except:
        print("Ошибка: введено не число")