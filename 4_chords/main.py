from scipy.misc import derivative
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


def f(x) -> float:
    """Целевая функция."""
    return 3 * x ** 4 + (x - 1) ** 2
print(derivative(f, 3))
print(derivative(f, 3))
print(derivative(f, 3, dx=1e-6))