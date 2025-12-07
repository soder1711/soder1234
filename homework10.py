class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.current_floor = bottom_floor
    def floor_up(self):
        self.current_floor += 1
        print(f"The elevator is now at floor {self.current_floor}")
    def floor_down(self):
        self.current_floor -= 1
        print(f"The elevator is now at floor {self.current_floor}")
    def go_to_floor(self, target):
        while target > self.current_floor:
            self.floor_up()
        while target < self.current_floor:
            self.floor_down()

class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.elevators = []
        for i in range(number_of_elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))
    def run_elevator(self, elevator_number, target):
        elevator = self.elevators[elevator_number - 1]
        elevator.go_to_floor(target)
    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(elevator.bottom_floor)

h = Elevator(1, 10)
h.go_to_floor(7)
h.go_to_floor(3)

building = Building(1, 15, 5)
building.run_elevator(1, 7)
building.run_elevator(4, 8)
building.fire_alarm()

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

import random

class Race:
    def __init__(self, name: str, distance: int, cars):
        self.name = name
        self.distance = distance
        self.cars = cars
    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)
    def race_finished(self):
        for car in self.cars:
            if car.get_travelled_distance() >= self.distance:
                return True
        return False
    def print_status(self):
        print(f"{'Registration Number':<23} {'Max Speed':<10} {'Current Speed':<15} {'Travelled Distance':<10}")
        print("-" * 70)
        for car in self.cars:
            print(f"{car.get_registration_number():<23} {car.get_maximum_speed():<10} "
                  f"{car.get_speed():<14} {car.get_travelled_distance():<18.0f}")

cars = []
for i in range(1, 11):
    max_speed = random.randint(100, 200)
    registration = f"ABC-{i}"
    cars.append(Car(max_speed, registration))
race = Race("Grand Demolition Derby", 8000, cars)
hours = 0
while not race.race_finished():
    hours += 1
    race.hour_passes()

    if hours % 10 == 0:
        print(f"--- Hour {hours} Status ---")
        race.print_status()