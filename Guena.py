import math
import matplotlib.pyplot as plt

def differential_equation(x, y):
    return x*math.e**((-x)**2) - 2*x*y

def Guena_method(x, y, h, n):
    x_values = [x]
    y_values = [y]
    print(f"{n}:  x = {round(x, 2)}; y = {round(y, 3)}")
    for i in range(n):
        y_im = y_values[i] + h * differential_equation(x, y_values[i])     #вычисляем yi+1 на i+1 шаге методом Эйлера через yi и значение x на прошлом шаге
        x += h
        y = y_values[i] + h/2*(differential_equation(x_values[i], y_values[i]) + differential_equation(x, y_im))   #Вычисляем значение yi+1 на i+1 шаге методом Гюна по yi и yi+1. y_im вычислено выше методом Эйлера
        x_values.append(x)
        y_values.append(y)
        print(f"{n}:  x = {round(x, 2)}; y = {round(y, 3)}")
    return x_values, y_values

# Параметры метода Эйлера
x0 = 0        # начальное значение x
y0 = 0        # начальное значение y
h = 0.05       # шаг
n = 20       # количество шагов

# Решаем уравнение методом Эйлера
x, y = Guena_method(x0, y0, h, n)

# Строим график результатов
plt.plot(x, y, label="решение дифф. уравнения")
plt.legend()
plt.title('Решение дифференциального уравнения методом Гюна')
plt.grid()
plt.show()
