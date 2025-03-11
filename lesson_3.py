def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m == 1:
        return n + 2
    elif m == 2:
        return 2 * n + 3
    elif m == 3:
        return 2**(n + 3) - 3
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

# Запрос ввода от пользователя
if __name__ == "__main__":
    try:
        m = int(input("Введите неотрицательное число m: "))
        n = int(input("Введите неотрицательное число n: "))
        
        if m < 0 or n < 0:
            print("Оба числа должны быть неотрицательными.")
        else:
            result = ackermann(m, n)
            print(f"A({m}, {n}) = {result}")
    except ValueError:
        print("Пожалуйста, введите целые неотрицательные числа.")