import sys
import math

class SquareRoots:

    def __init__(self):
        '''
        Конструктор класса
        '''
        # Объявление коэффициентов
        self.coef_A = 0.0
        self.coef_B = 0.0
        self.coef_C = 0.0
        # Количество корней
        self.num_roots = 0
        # Список корней
        self.roots_list = []

    def get_coef(self, index, prompt):
        '''
        Читаем коэффициент из командной строки или вводим с клавиатуры
        Args:
            index (int): Номер параметра в командной строке
            prompt (str): Приглашение для ввода коэффицента
        Returns:
            float: Коэффициент квадратного уравнения
        '''
        try:
            # Пробуем прочитать коэффициент из командной строки
            coef_str = sys.argv[index]
        except:
            # Вводим с клавиатуры
            print(prompt)
            coef_str = input()
        # Переводим строку в действительное число
        coef = float(coef_str)
        return coef

    def get_coefs(self):
        '''
        Чтение трех коэффициентов
        '''
        self.coef_A = self.get_coef(1, 'Введите коэффициент А:')
        self.coef_B = self.get_coef(2, 'Введите коэффициент B:')
        self.coef_C = self.get_coef(3, 'Введите коэффициент C:')

    def calculate_roots(self):
        '''
        Вычисление корней квадратного уравнения
        '''
        a = self.coef_A
        b = self.coef_B
        c = self.coef_C
        # Вычисление дискриминанта и корней
        D = b*b - 4*a*c
        if D == 0.0:
            root = -b / (2.0*a)
            D_2 = -4*(-root)
            if D_2 == 0.0:
                root1 = 0
                self.num_roots = 1
                self.roots_list.append(root1)
            elif D_2 > 0:
                sqD = math.sqrt(D_2)
                root1 = sqD / 2.0
                root2 = -sqD / 2.0
                self.num_roots = 2
                self.roots_list.append(root1)
                self.roots_list.append(root2)

        elif D > 0.0:
            sqD = math.sqrt(D)
            root1 = (-b + sqD) / (2.0*a)
            root2 = (-b - sqD) / (2.0*a)
            D_2 = -4 * (-root1)
            D_3 = -4 * (-root2)
            if (D_2 == 0) and (D_3 > 0):
                root3 = 0
                sqD = math.sqrt(D_3)
                root4 = sqD / 2.0
                root5 = -sqD / 2.0
                self.num_roots = 3
                self.roots_list.append(root3)
                self.roots_list.append(root4)
                self.roots_list.append(root5)
            elif (D_2 > 0) and (D_3 == 0):
                root3 = 0
                sqD = math.sqrt(D_2)
                root4 = sqD / 2.0
                root5 = -sqD / 2.0
                self.num_roots = 3
                self.roots_list.append(root3)
                self.roots_list.append(root4)
                self.roots_list.append(root5)
            elif (D_2 > 0) and (D_3 > 0):
                sqD_1 = math.sqrt(D_2)
                root3 = sqD_1 / 2.0
                root4 = -sqD_1 / 2.0
                sqD_2 = math.sqrt(D_3)
                root5 = sqD_2 / 2.0
                root6 = -sqD_2 / 2.0
                self.num_roots = 4
                self.roots_list.append(root3)
                self.roots_list.append(root4)
                self.roots_list.append(root5)
                self.roots_list.append(root6)
            elif (D_2 < 0) and (D_3 > 0):
                sqD = math.sqrt(D_3)
                root4 = sqD / 2.0
                root5 = -sqD / 2.0
                self.num_roots = 2
                self.roots_list.append(root4)
                self.roots_list.append(root5)
            elif (D_2 > 0) and (D_3 < 0):
                sqD = math.sqrt(D_2)
                root4 = sqD / 2.0
                root5 = -sqD / 2.0
                self.num_roots = 2
                self.roots_list.append(root4)
                self.roots_list.append(root5)


    def print_roots(self):
        # Проверка отсутствия ошибок при вычислении корней
        if self.num_roots != len(self.roots_list):
            print(('Ошибка. Уравнение содержит {} действительных корней, ' + 'но было вычислено {} корней.').format(self.num_roots, len(self.roots_list)))
        else:
            if self.num_roots == 0:
                print('Нет корней')
            elif self.num_roots == 1:
                print('Один корень: {}'.format(self.roots_list[0]))
            elif self.num_roots == 2:
                print('Два корня: {} и {}'.format(self.roots_list[0], self.roots_list[1]))
            elif self.num_roots == 3:
                print('Три корня: {}, {} и {}'.format(self.roots_list[0], self.roots_list[1], self.roots_list[2]))
            elif self.num_roots == 4:
                print('Четыре корня: {}, {}, {} и {}'.format(self.roots_list[0], self.roots_list[1], self.roots_list[2], self.roots_list[3]))



def main():
    '''
    Основная функция
    '''
    # Создание объекта класса
    r = SquareRoots()
    # Последовательный вызов необходимых методов
    r.get_coefs()
    r.calculate_roots()
    r.print_roots()

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()