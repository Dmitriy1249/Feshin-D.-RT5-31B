import time
import contextlib

def timer(func):
    """Декоратор для измерения времени выполнения функции."""
    @contextlib.contextmanager
    def context_manager(*args, **kwargs):
        start_time = time.perf_counter()  # Более точное измерение времени
        yield
        end_time = time.perf_counter()
        print(f"Время выполнения функции {func.__name__}: {end_time - start_time:.5f} секунд")
    return context_manager

@timer
def my_long_function():
    # Какая-то долгая операция
    for _ in range(1000000):
        pass

if __name__ == '__main__':
    with my_long_function():
        pass