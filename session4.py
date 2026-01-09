'''
Write a Python program that declares a class describing your favorite animal. Have the data members of the class represent the following physical parameters of the animal: length of the arms (float), length of the legs (float), number of eyes (int), does it have a tail? (bool), is it furry? (bool). Write an initialization function that sets the values of the data members when an instance of the class is created. Write a member function of the class to print out and describe the data members representing the physical characteristics of the animal
'''
class Animal:
    def __init__(self, arm_len, leg_len, num_eyes, has_tail, is_furry):
        self.arm_len = arm_len
        self.leg_len = leg_len
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def __str__(self):
        return(f"My favorite animal has an arm and leg length of {self.arm_len}cm and {self.leg_len}cm respectively. It has {self.num_eyes} eye{"s" if self.num_eyes > 1 else ""}, has {"a" if self.has_tail else "no"} tail, and is{"n't" if not self.is_furry else ""} furry.")

dog = Animal(20.5,20.1,2,True,False)
print(dog)
