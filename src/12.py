import random
class School(object):
    def __init__(self, name, location):
        self.name = name
        self.location = location
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name is required")
        self._name = value
    
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, value):
        if not value:
            raise ValueError("Location is required")
        self._location = value
    
    def __str__(self):
        return f"{self.name} at {self.location}"
    
school_list = []
for i in range(random.randint(5, 10)):
    name = "".join([chr(random.randint(97, 122)) for _ in range(random.randint(3, 6))])
    location = "".join([chr(random.randint(97, 122)) for _ in range(random.randint(5, 8))])
    school_list.append(School(name, location))
print(school_list)