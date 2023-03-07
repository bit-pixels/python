class car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color


    def drive(self):
        print("This car is driving")
    def stop(self):
        print("This car has stopped")
