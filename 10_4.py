# 1

# people = int(input('Введите количество людей: '))
#
# for hour in range(people + 1):
#     print('Идет час: ', hour)
#     for num in range(hour, people):
#         print('Номер в очереди: ', num)
#     print()
# print('Очередь обслужена!')


# 2

# seqNum = int(input('Сколько будет чисел? '))
# numeral = int(input('Какую цифру считать? '))
#
# while numeral < 0 or numeral > 9:
#     print('Вы вели неправельную цифру, введите цифру от 0 до 9. Введите новую цифру: ', end='')
#     numeral = int(input())
#
# numeralCount = 0
# for num in range(seqNum):
#     number = int(input('ведите число: '))
#     while number > 0:
#         if number % 10 == numeral:
#             numeralCount += 1
#         number //= 10
# print('Цифр', numeral, 'в последовательности: ', numeralCount)

# 3

number = int(input('Введите число: '))

for row in range(number + 1):
    for col in range(row, number +1):
        print(col, end=' ')
    print()