# Запрос у пользователя значений M и N
M = int(input("Введите значение M (начало диапазона): "))
N = int(input("Введите значение N (конец диапазона): "))

# Проверка на то, что M меньше N и оба значения натуральные
if M < 1 or N < 1:
    print("M и N должны быть натуральными числами (больше 0).")
elif M > N:
    print("M должно быть меньше или равно N.")
else:
    print(f"Натуральные числа в промежутке от {M} до {N}:")
    for i in range(M, N + 1):
        print(i)