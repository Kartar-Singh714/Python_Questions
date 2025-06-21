class Area_Of_Circle:
    pi = 3.1415
    def __init__(self, radius):
        self.radius = radius

    def area_circle(self):
        area = 2 * self.pi * self.radius
        return round(area, 3)

    def circum_circle(self):
        circum = self.pi * (self.radius ** 2)
        return round(circum, 3)


radius = input("Please enter the Radius of the circle: ")
if radius.replace(".", "").isdigit() and float(radius) > 0.0:
    radius = float(radius)
    circle1 = Area_Of_Circle(radius)
    print(f"Area of Circle is: {circle1.area_circle()} \nCicumference of Circle is: {circle1.circum_circle()}")
else:
    print("Invalid Radius")