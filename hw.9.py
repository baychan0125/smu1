class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return self.x, self.y

    def show(self):
        print(f'({self.x}, {self.y})')

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.left_top = Point(x1, y1)
        self.right_bottom = Point(x2, y2)

    def getWidth(self):
        return abs(self.right_bottom.x - self.left_top.x)

    def getHeight(self):
        return abs(self.right_bottom.y - self.left_top.y)

    def getArea(self):
        return self.getWidth() * self.getHeight()

    def getPerimeter(self):
        return 2 * (self.getWidth() + self.getHeight())

    def show(self):
        print("좌측 상단 꼭지점:", end=" ")
        self.left_top.show()
        print("우측 하단 꼭지점:", end=" ")
        self.right_bottom.show()


if __name__ == "__main__":
    r1 = Rectangle(5, 5, 20, 10)
    a = r1.getArea()
    p = r1.getPerimeter()

    r1.show()
    print(f"넓이는 {a}, 둘레는 {p}")
