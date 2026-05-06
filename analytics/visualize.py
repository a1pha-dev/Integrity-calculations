import numpy as np
from matplotlib import pyplot as plt
plt.style.use('ggplot')


def function(x):
    return 1 / (x * np.sqrt(1 - np.log(x)))


def plot_function():
    x = np.linspace(0.5, np.e - 0.5, 1000)
    y = function(x)
    interval = np.linspace(1, np.sqrt(np.e), 100)

    plt.figure(figsize=(12, 6))

    plt.plot(x, y, label='$f(x)$')
    plt.fill_between(interval, function(interval), alpha=0.5)
    plt.axvline(1, color='blue', linestyle='--', label="Пределы интегрирования")
    plt.axvline(np.sqrt(np.e), color='blue', linestyle='--')

    plt.title(r'Подынтегральная функция $\frac{1}{x\sqrt{1 - \ln x}}$')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    plot_function()