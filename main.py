from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


if __name__ == '__main__':
    N = 21

    rect = Rectangle(N, N, 'blue')
    circle = Circle(N, 'green')
    square = Square(N, 'red')

    print(rect)
    print(circle)
    print(square)

