import json
import sys
from random import randint
import time
import contextlib

def timer(func):
    """Декоратор для измерения времени выполнения функции."""
    @contextlib.contextmanager
    def context_manager(*args, **kwargs):
        start_time = time.perf_counter()
        yield
        end_time = time.perf_counter()
        print(f"Время выполнения функции {func.__name__}: {end_time - start_time:.5f} секунд")
    return context_manager

def print_result(func):
    """Декоратор для печати результата функции."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(func.__name__)
        print(result)
        return result
    return wrapper

def load_data(path):
    """Загружает данные из JSON-файла."""
    with open(path) as f:
        return json.load(f)

@print_result
@timer
def process_data(data):

    # Извлечение уникальных профессий
    unique_jobs = sorted(set(item['job_title'].lower() for item in data), key=str.casefold)

    # Фильтрация программистов
    programmers = list(filter(lambda x: x['job_title'].lower().startswith('программист'), data))

    # Добавление опыта Python
    programmers_with_python = list(map(lambda x: x['job_title'] + ' с опытом Python', programmers))

    # Генерация зарплат и формирование итогового результата
    salaries = (randint(100000, 200000) for _ in programmers_with_python)
    result = [f"{job}, зарплата {salary} руб." for job, salary in zip(programmers_with_python, salaries)]
    return result

if __name__ == '__main__':
    path = sys.argv[1]
    data = load_data(path)
    process_data(data)