import numpy as np
import pandas as pd
from scipy import integrate

from visualize import function

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)

_METHODS = ["quad", "simpson", "trapezoid"]
_COLUMNS = []
for method in _METHODS:
    _COLUMNS.append(method)
    _COLUMNS.append(f"{method}_abs_error")
    _COLUMNS.append(f"{method}_rel_error")


def calculate_integral(f, a, b, limit):
    quad, _ = integrate.quad(f, a, b, limit=limit)

    x = np.linspace(a, b, limit + 1)
    simpson = integrate.simpson(f(x), x)
    trapezoid = integrate.trapezoid(f(x), x)

    return {"quad": quad, "simpson": simpson, "trapezoid": trapezoid}


def collect_results(limits=(14, 50), answer=2 - np.sqrt(2)):
    results = {}
    for col in _COLUMNS:
        results[col] = {}

    for limit in limits:
        result = calculate_integral(function, 1, np.sqrt(np.e), limit)
        for method in result:
            results[method][f"precision_{limit}"] = result[method]
            results[f"{method}_abs_error"][f"precision_{limit}"] = np.abs(result[method] - answer)
            results[f"{method}_rel_error"][f"precision_{limit}"] = np.abs(result[method] - answer) / np.abs(answer)

    return pd.DataFrame(results)


def main():
    limits  = tuple(map(int, input("Укажите число разбиений: ").split()))
    results = collect_results(limits)
    print(results)


if __name__ == "__main__":
    main()