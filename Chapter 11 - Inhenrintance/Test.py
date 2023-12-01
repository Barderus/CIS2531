class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def calcArea(self):
        return self.__width * self.__height

class Cuboid(Rectangle):
    def __init__(self, width, height, length):
        super().__init__(width, height)
        self.__length = length

    def calcVolume(self):
        return self.__width * self.__height * self.__length


if __name__ == "__main__":
    figure = Cuboid(10, 12, 15)
    print(figure.calcVolume())
