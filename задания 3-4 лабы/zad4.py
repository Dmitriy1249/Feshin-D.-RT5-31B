data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    # Сортировка с использованием lambda-функции
    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)

    # Сортировка без использования lambda-функции
    def key_function(x):
        return abs(x)
    result = sorted(data, key=key_function, reverse=True)

    print(result)
    print(result_with_lambda)