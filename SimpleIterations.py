import math
import matplotlib as plt
import numpy as np

def simple_iteration_method(x0, epsilon):
    xi = x0             #берем начальное значение

    while True:
        xi_prev = xi                    #Сохраняем его
        xi = 1 - 2*math.e**xi_prev   #Вычисляем следующее приближение. Надо выразить в форме x = f(x)

        print(f"Прошлое: {round(xi_prev, 5)}, текущее: {round(xi, 5)}, разница: {abs(round(xi - xi_prev, 5))}")
        if abs(xi - xi_prev) < epsilon:         #проверяем, что разница больше заданной точности
            print(f"Корень: {round(xi, 5)}")
            return xi

def plot_root(f, x0):         #тут мы выводим график
    x = np.linspace(x0 - 1, x0 + 1, 1000) #Вычисляем массив точек для интервала от x0-1 до x0+1 с количеством точек 1000.
    y = f(x)
    plt.plot(x, y)
    plt.grid(True)


simple_iteration_method(1, 0.1)    #Задаем начальное значение на интервале и точность

