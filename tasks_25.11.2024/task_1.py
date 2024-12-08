class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value <= 0:
            print("Ширина должна быть положительной")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value <= 0:
            print("Высота должна быть положительной")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

rect = Rectangle(5, 10)

rect.width = 15

print("Площадь:", rect.area())



