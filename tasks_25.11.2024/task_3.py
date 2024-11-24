class Circle:
    def __init__(self, value):
        self.radius = value

    def set_diameter(self, diameter):
        if diameter <= 0:
            print("Диаметр не может быть отрицательным или равен нулю")
        else:
            self.radius = diameter / 2
            return self.radius

    def area(self):
        if self.radius <= 0:
            print("Радиус не может быть отрицательным или равен нулю")
        else:
            return 3.14 * self.radius ** 2

circle = Circle(5)
circle.set_diameter(10)
print(circle.area())