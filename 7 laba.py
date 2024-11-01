import numpy as np

# Константы
eps = 1e-6
V = 16.0

# Функция f
def f(x, y):
    return 2 * V * x + V * x ** 2 - y

# Функция для проверки значения y на основе x
def check_y(x):
    return V * x ** 2

# Метод Эйлера
def euler(n, h, x0, y0):
    x = np.zeros(n)
    y = np.zeros(n)
    
    # Инициализация начальных значений
    x[0] = x0
    y[0] = y0
    
    # Заполнение массива x и вычисление значений y
    for i in range(n - 1):
        x[i + 1] = x[i] + h
        y[i + 1] = y[i] + h * f(x[i], y[i])
    
    return y

# Расширенный метод Эйлера
def ex_euler(n, h, x0, y0):
    x = np.zeros(2 * n)
    y = np.zeros(2 * n)
    
    # Инициализация начальных значений
    x[0] = x0
    y[0] = y0
    
    # Заполнение массива x с шагом h/2
    for i in range(2 * n - 1):
        x[i + 1] = x[i] + h / 2
    
    # Вычисление значений y по расширенному методу Эйлера
    for i in range(2 * n - 1):
        if i % 2:
            y[i + 1] = y[i - 1] + h * f(x[i], y[i])
        else:
            y[i + 1] = y[i] + h / 2 * f(x[i], y[i])
    
    return y[::2]

# Метод предварительного и корректирующего счета
def pre_corr(n, h, x0, y0):
    x = np.zeros(n)
    y = np.zeros(n)
    
    # Инициализация начальных значений
    x[0] = x0
    y[0] = y0
    
    # Заполнение массива x и расчет значений y
    for i in range(n - 1):
        x[i + 1] = x[i] + h
        y[i + 1] = y[i] + h * f(x[i], y[i])
        # Корректировка значения y
        y[i + 1] += (h / 2) * (f(x[i], y[i]) + f(x[i + 1], y[i + 1]))
    
    return y

# Функция для вывода результатов
def print_results(vx, vy):
    # Вывод x и y
    print("x:", "\t".join(f"{xi:.5f}" for xi in vx))
    print("y:", "\t".join(f"{yi:.5f}" for yi in vy))
    
    # Вывод y, рассчитанных через check_y
    check_y_values = [check_y(xi) for xi in vx]
    print("\n tochn_y(x):", "\t".join(f"{cy:.5f}" for cy in check_y_values))
    
    # Вывод отклонений
    deviations = [vy[i] - check_y_values[i] for i in range(len(vy))]
    print("\n Отклонения:", "\t".join(f"{d:.5f}" for d in deviations))
    
    # Поиск максимального отклонения
    max_deviation = max(abs(d) for d in deviations)
    print(f"\n Максимальное отклонение: {max_deviation:.5f}")

def solve():
    n = 9  # Количество шагов
    h = 1.0  # Шаг по оси X
    x0 = 1.0  # Начальное значение X
    y0 = V  # Начальное значение Y

    vx = np.linspace(x0, x0 + (n - 1) * h, n)
    
    print("Метод Эйлера: \n")
    vy1 = euler(n, h, x0, y0)
    print_results(vx, vy1)
    print("\n")

    print("Расширенный метод Эйлера: \n")
    vy2 = ex_euler(n, h, x0, y0)
    print_results(vx, vy2)
    print("\n")

if __name__ == "__main__":
    solve()
