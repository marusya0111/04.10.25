# Создайте декоратор retry(max_retries, delay), который принимает два аргумента:
# максимальное количество попыток и задержку между попытками.

# Декоратор должен принимать от функции возвращаемое значение, и если значение False,
# то запускать функцию снова через количество секунд, переданное в параметре delay, пока возвращаемое
# значение не будет True,
# при этом количество перезапусков не должно превышать значения, переданного в параметре max_retries.
from time import time
start = time.time()
end = time.time()
b = end- start

def retry(max_retries,delay):
    def decorator(func):
        def wrapper(*args, **kwargs):
            trial = 0
            while trial <max_retries:
                result = func(*args, **kwargs)
                return result
            trial += 1
            if trial >= max_retries:
                return False
                global b
                delay = b
        return wrapper
    return decorator












