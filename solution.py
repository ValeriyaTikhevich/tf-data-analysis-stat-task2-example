import pandas as pd
import numpy as np

from scipy.stats import laplace


chat_id = 998964007 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    x = x / (17*17)
    return x + 0.5 - alpha, \
           x - 0.5 + alpha
