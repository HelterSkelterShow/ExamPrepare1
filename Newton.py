import matplotlib.pyplot as plt
import numpy as np
import math

def f(x):
    return 2* math.e**x +x-1  #ввод функции

def df(x):
    return 2*math.e**x + 1     #ввод производной функции

def newton(f, df, x0, tol=1e-6):    #max_iter - максимальное число шагов
    fx0 = f(x0)
    dfx0 = df(x0)
    xi = x0 - fx0/dfx0
    if abs(xi - x0) <= tol:      #проверка условия |xi - x0| <= погрешности
        return xi
    return newton(f, df, xi)    #реккурентный вызов функции

def plot_root(f, x0):         #тут мы выводим график
    x = np.linspace(x0 - 1, x0 + 1, 1000) #Вычисляем массив точек для интервала от x0-1 до x0+1 с количеством точек 1000.
    y = f(x)
    plt.plot(x, y)
    plt.grid(True)

root = newton(f, df, 2)  #тут мы последним аргументом вводим наше значение
print(f"Корень уравнения: {round(root, 5)}")
plot_root(f, 2)      #тут мы аргументом вводим наше значение
plt.show()