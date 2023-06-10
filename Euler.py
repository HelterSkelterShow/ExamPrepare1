import math
import matplotlib.pyplot as plt

def differential_equation(x, y):
    return x*math.e**((-x)**2) - 2*x*y

def euler_method(x, y, h, n):
    x_values = [x]
    y_values = [y]
    print(f"{n}:  x = {round(x, 2)}; y = {round(y, 3)}")
    for i in range(n):
        y += h * differential_equation(x, y)
        x += h
        print(f"{n}:  x = {round(x, 2)}; y = {round(y, 3)}")
        x_values.append(x)
        y_values.append(y)
    return x_values, y_values

# Параметры метода Эйлера
x0 = 0        # начальное значение x
y0 = 0        # начальное значение y
h = 0.05       # шаг
n = 20       # количество шагов

# Решаем уравнение методом Эйлера
x, y = euler_method(x0, y0, h, n)

# Строим график результатов
plt.plot(x, y, label="решение дифф. уравнения")
plt.legend()
plt.title('Решение дифференциального уравнения методом Эйлера')
plt.grid()
plt.show()
