#!/usr/bin/env python3

class Dog:
    def bark(self):
        print("Woof!") 

    def sit(self):
        print(f"The dog is sitting.")
        
    #Instance method definition
fido = Dog()
fido.bark()

snoopy = Dog()
snoopy.bark()
snoopy.sit()