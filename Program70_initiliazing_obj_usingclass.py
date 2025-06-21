class Car_Design:
    def __init__(self, model, manufacturing_year, city):
        self.model =model
        self.manufacturing_year = manufacturing_year
        self.delivered_city = city


car_1 = Car_Design("Alpha", 2024, "Delhi")
print(f"Manufacturing Year of Car is: {car_1.manufacturing_year}")
print(f"Model of Car is: {car_1.model}\n")

car_2 = Car_Design("ZXI", 2021, "Gurugram")
print(f"Car is delivered in: {car_1.delivered_city}")
print(f"Manufacturing Year of Car is: {car_1.manufacturing_year}")