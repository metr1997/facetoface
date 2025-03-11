def sum_of_natural_numbers(M, N):
    # Убедимся, что M меньше или равен N
    if M > N:
        M, N = N, M

    # Начинаем сумму с 0
    total_sum = 0

    # Проходим по всем числам от M до N
    for number in range(M, N + 1):
        # Проверяем, является ли число натуральным
        if number > 0:
            total_sum += number

    return total_sum

# Пример использования:
try:
    M = int(input("Введите M (начало промежутка): "))
    N = int(input("Введите N (конец промежутка): "))

    if M < 1 or N < 1:
        print("Пожалуйста, введите натуральные числа (больше 0).")
    else:
        result = sum_of_natural_numbers(M, N)
        print(f"Сумма натуральных чисел от {M} до {N} равна: {result}")
except ValueError:
    print("Пожалуйста, введите корректные целые числа.")