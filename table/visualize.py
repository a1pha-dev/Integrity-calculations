import pandas as pd
from matplotlib import pyplot as plt
plt.style.use('ggplot')


def function():
    data = pd.read_csv("data.csv")
    x = data['x']
    y = data['y']

    return x, y


def plot_function():
    x, y = function()

    plt.figure(figsize=(12, 6))
    plt.scatter(x, y, label='$f(x)$')
    plt.title('Подынтегральная функция')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    plot_function()