# Практическая №6


# Ввод количества точек
n = int(input("Введите кол-во точек - "))
n = n - 1  

# Списки для хранения точек
x_points = []
y_points = []


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
print("Найти значение?")
print("1 - Да")
print("2 - Нет")
choice = input("1 - 2 - ")


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


# Полином
print("")
print("ПОЛИНОМ ЛАГРАНЖА:")
print("P(x) = ", end="")
for i in range(n + 1):
    # Выводи
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
    x_find = float(input("Введите x - "))
    y_result = lagrange(x_find)
    print("")
    print(f"P({x_find}) = {y_result}")

    # Проверить точность в узлах
    print("")
    print("Проверка в узлах -")
    for i in range(n + 1):
        check = lagrange(x_points[i])

        print(f"P({x_points[i]}) = {check} (итог {y_points[i]})")
