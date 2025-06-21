# Rectangle Geometry
# Create a class Rectangle with attributes length and breadth.
# Write methods to calculate and return the area and perimeter of the rectangle.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area_of_rectangle(self):
        area= self.length * self.breadth
        return area

    def perimeter_of_rectangle(self):
        perimeter = 2 * (self.length + self.breadth)
        return perimeter

le = input("Please enter the length of the Rectangle: ")
bre = input("Please enter the breadth of the Rectangle: ")

if le.replace(".", "").isdigit() and  bre.replace(".", "").isdigit() and float(le) >0 and float(bre)>0:
    length = float(le)
    breadth = float(bre)
    rectangle1 = Rectangle(int(le), int(bre))
    print(f"The Area of rectangle = {rectangle1.area_of_rectangle()}\nThe Perimeter of rectangle is: {rectangle1.perimeter_of_rectangle()}")
else:
    print("Invalid Inputs")