import random

def gen_random(num_count, begin, end):

    for _ in range(num_count):
        yield random.randint(begin, end)

# Сгенерируем 5 случайных чисел от 1 до 10
for number in gen_random(5, 1, 10):
    print(number)