from datetime import datetime
import math

class Person:
    def __init__(self, first_name, last_name, birth_year) -> None:
        self._age = None
        self._birth_year = birth_year
        self._first_name = first_name
        self._last_name = last_name
        self._salary = 55000
        self._bonus_percent = 10
        self._current_year = datetime.now().year

    @property
    def current_year(self):
        return self._current_year

    def get_birth_year(self):
        return self._birth_year
    def set_birth_year(self, birth_year):
        self._birth_year = birth_year
        self._age = None
    birth_year = property(fget=get_birth_year, fset=set_birth_year)

    def get_age(self):
        return self._age
    def get_age(self):
        if self._age is None:
            self._age = self.current_year - self._birth_year
            return self._age
        return self._age
    age = property(fget=get_age)

    def get_full_name(self):
        return self._first_name + " " + self._last_name
    def set_full_name(self, full_name):
        self._first_name, self._last_name = full_name.split()
    full_name = property(fget=get_full_name, fset=set_full_name)

    @property
    def first_name(self):
        return self._first_name
    @property
    def last_name(self):
        return self._last_name

    def get_base_salary(self):
        return self.salary - self.bonus
    def set_base_salary(self, base_salary):
        self._base_salary = base_salary
        self._bonus = base_salary * (self._bonus_percent/100)
        self._salary = self._base_salary + self._bonus
    base_salary = property(fget=get_base_salary, fset=set_base_salary)

    def get_bonus(self):
        return self.salary * (self._bonus_percent / 100)
    def set_bonus(self):
        self._bonus = (self._base_salary * self._bonus_percent)/100
        self._salary = self.base_salary + self._bonus
    bonus = property(fget=get_bonus, fset=set_bonus)
    
    def get_salary(self):
        return self._salary
    def set_salary(self, salary):
        self._salary = salary
        self._bonus = salary * (self.bonus/100)
        self._base_salary = salary - self._bonus
    salary = property(fget=get_salary, fset=set_salary)


class Circle:
    def __init__(self, radius) -> None:
        self._radius = radius
        self._area = None
        self._diameter = None

    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError
        self._area = None
        self._diameter = None
        self._radius = value

    @property
    def diameter(self):
        if self._diameter is None:
            return self.radius * 2
        return self._diameter
    
    @property
    def area(self):
        if self._area is None:
            return (self.radius**2) * math.pi
        return self._area
    

class Vehicle:
    vehicle_count = 0

    def __init__(self, make, model, year) -> None:
        self._make = make
        self._model = model
        self._year = year
        Vehicle.vehicle_count += 1

    @classmethod
    def get_vehicle_count(cls):
        return cls.vehicle_count
    
    @staticmethod
    def classify_vehicle(type:str):
        return f"This is a {type}"
    
class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year) -> None:
        super().__init__(make, model, year)

    @staticmethod
    def classify_vehicle(type: str):
        return f"This is an electric {type}"
    

class DynamicClass:
    static_value = None

    def __init__(self, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)

    def dynamic_attr(self, name, value):
        setattr(self, name, value)

class ValidatedAttribute:
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, int) or val <= 0:
            raise ValueError("Value must be a positive integer.")
        self._value = val