class dog:
    def __init__(self,name, age, race,sound):
        self.name = name
        self.age = int(age)
        self.race = race
        self.sound = sound

    def get_name(self):
        return self.name
        
    def get_age(self):
        return self.age
        
    def get_race(self):
        return self.race
        
    def get_sound(self):
        return self.race
        
    def attack_mode(self):
        return print(f"{self.name} is angry and starts barking {self.sound} and then attacks you....")
        
####################################

class cat:
    def __init__(self,name, age, race,sound):
        self.name = name
        self.age = int(age)
        self.race = race
        self.sound = sound

    def get_name(self):
        return self.name
        
    def get_age(self):
        return self.age
        
    def get_race(self):
        return self.race
        
    def get_sound(self):
        return self.race
        
    def attack_mode(self):
        return print(f"{self.name} is angry and starts barking {self.sound} and then attacks you....")
        

####################################

class Spiderman:
    def __init__(self,name,age,sound):
        self.name = name
        self.age = age
        self.sound = sound
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_sound(self):
        return self.sound
    
    def attack():
        print("Attacking with 10 damage.")

    def defend():
        print("Defending shield")
    

####################################


import math

class Rectangle:
    def __init__(self, width, weight):
        self.width = width
        self.weight = weight

    def calculate_area(self):
        return self.width * self.weight
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.weight)

    def print_details(self):
        print(f"Rectangle Details:")
        print(f"Width: {self.width}")
        print(f"Height: {self.weight}")
        print(f"Area: {self.calculate_area()}")
        print(f"Perimeter: {self.calculate_perimeter()}")

    
####################################


class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def calculate_circumference(self):
        return 2 * math.pi * self.radius
    
    def print_details(self):
        print(f"Circle Details:")
        print(f"Radius: {self.radius}")
        print(f"Area: {self.calculate_area()}")
        print(f"Circumference: {self.calculate_circumference()}")
    

    