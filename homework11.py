class Publication:
    def __init__(self, name: str):
        self.name = name


class Book(Publication):
    def __init__(self, name, author: str, page_count: int):
        super().__init__(name)
        self.author = author
        self.page_count = page_count
    def print_information(self):
        print(self.name)
        print(self.author)
        print(self.page_count)

class Magazine(Publication):
    def __init__(self, name: str, chief_editor: str):
        super().__init__(name)
        self.chief_editor = chief_editor
    def print_information(self):
        print(self.name)
        print(self.chief_editor)

magazine1 = Magazine("Donald Duck", "Aki Hyyppä")
book1 = Book("Compartment No. 6", "Rosa Liksom", 192)
magazine1.print_information()
book1.print_information()



class Car:
    def __init__(self, maximum_speed: int, registration_number: str):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.travelled_distance = 0
        self.speed = 0
    def get_maximum_speed(self):
        return self.maximum_speed
    def get_registration_number(self):
        return self.registration_number
    def get_travelled_distance(self):
        return self.travelled_distance
    def get_speed(self):
        return self.speed
    def accelerate(self, change):
        self.speed += change
        if self.speed > self.maximum_speed:
            self.speed = self.maximum_speed
        if self.speed < 0:
            self.speed = 0
    def drive(self, hours: float):
        self.travelled_distance += self.speed * hours

class ElectricCar(Car):
    def __init__(self, maximum_speed, registration_number, battery_capacity):
        super().__init__(maximum_speed, registration_number)
        self.batter_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, maximum_speed, registration_number, tank_volume):
        super().__init__(maximum_speed, registration_number)
        self.tank_volume = tank_volume

electric_car1 = ElectricCar(180, "ABC-15", 52.5)
gasoline_car1 = GasolineCar(165, "ACD-123", 32)

electric_car1.accelerate(110)
gasoline_car1.accelerate(120)

electric_car1.drive(3)
gasoline_car1.drive(3)

print(electric_car1.get_travelled_distance())
print(gasoline_car1.get_travelled_distance())