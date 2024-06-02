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
        