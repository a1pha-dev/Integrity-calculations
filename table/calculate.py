import numpy as np
import pandas as pd
from scipy import integrate

from visualize import function

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)

_METHODS = ["simpson", "trapezoid"]
_COLUMNS = []
for method in _METHODS:
    _COLUMNS.append(method)
    _COLUMNS.append(f"{method}_abs_error")
    _COLUMNS.append(f"{method}_rel_error")


def calculate_integral(x, y):
    simpson = integrate.simpson(y, x)
    trapezoid = integrate.trapezoid(y, x)

    return {"simpson": simpson, "trapezoid": trapezoid}


def collect_results(answer=0.2 * (-3 + 2 * np.exp(np.pi / 2))):
    results = {}
    for col in _COLUMNS:
        results[col] = {}
    x, y = function()

    result = calculate_integral(x, y)
    for method in result:
        results[str(method)] = result[method]
        results[f"{method}_abs_error"] = np.abs(result[method] - answer)
        results[f"{method}_rel_error"] = np.abs(result[method] - answer) / np.abs(answer)

    return pd.DataFrame(results, index=[""])


def main():
    results = collect_results()
    print(results)


if __name__ == "__main__":
    main()
