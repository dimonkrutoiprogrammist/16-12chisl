# Ввод количества точек
n = int(input("Сколько точек у вас есть? (n+1 точек): "))
n = n - 1  # Переходим к n (степень полинома)

# Списки для хранения точек
x_points = []
y_points = []

print("")
print("Вводите точки (x, y):")
for i in range(n + 1):
    print(f"Точка {i + 1}:")
    x = float(input(f"  x{i} = "))
    y = float(input(f"  y{i} = "))
    x_points.append(x)
    y_points.append(y)

print("")
print("Ваши точки:")
for i in range(n + 1):
    print(f"({x_points[i]}, {y_points[i]})")

print("")
print("Хотите найти значение в какой-то точке?")
print("1 - Да, найти значение P(x)")
print("2 - Нет, показать только полином")
choice = input("Ваш выбор (1 или 2): ")


# Функция для вычисления полинома Лагранжа в точке xx
def lagrange(xx):
    result = 0.0
    for i in range(n + 1):
        # Считаем базисный полином L_i(x)
        L = 1.0
        for j in range(n + 1):
            if i != j:
                L = L * (xx - x_points[j]) / (x_points[i] - x_points[j])
        # Добавляем к результату
        result = result + y_points[i] * L
    return result


# Показать полином
print("")
print("ПОЛИНОМ ЛАГРАНЖА:")
print("P(x) = ", end="")
for i in range(n + 1):
    # Выводим yi * Li(x)
    print(f"{y_points[i]} * L{i}(x)", end="")
    if i < n:
        print(" + ", end="")
print("")

print("")
print("где:")
for i in range(n + 1):
    print(f"L{i}(x) = ", end="")
    for j in range(n + 1):
        if i != j:
            print(f"(x - {x_points[j]})", end="")
            if j < n and (j != i or i == n):
                print(" * ", end="")
    print(" / ", end="")
    for j in range(n + 1):
        if i != j:
            print(f"({x_points[i]} - {x_points[j]})", end="")
            if j < n and (j != i or i == n):
                print(" * ", end="")
    print("")

if choice == "1":
    print("")
    # Найти значение в точке
    x_find = float(input("Введите x, для которого найти P(x): "))
    y_result = lagrange(x_find)
    print("")
    print(f"P({x_find}) = {y_result}")

    # Проверить точность в узлах
    print("")
    print("Проверка в узлах (должно совпадать с y_i):")
    for i in range(n + 1):
        check = lagrange(x_points[i])
        print(f"P({x_points[i]}) = {check} (должно быть {y_points[i]})")