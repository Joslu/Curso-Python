# Programación orientada a objetos con Python
# Class is the blueprint from which individual objects are created. 
# Objects are a representation of real world objects like cars, dogs or bikes

# Python, as an Object-Oriented programming language, has these concepts: class and object.

#Python sintax for classes

class Robot:
    def __init__(self,name,color,weight): #Constructor method
        self.name = name
        self.color = color
        self.weight = weight

    def Introduce_Self(self):
        print("My name is " + self.name)
    
    def SayColor(self):
        print(f"My color is : {self.color}")

class Person:
    def __init__(self,n,p,i,r):
        self.name = n
        self.personality = p
        self.is_sitting = i
        self.robot = r

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False

    def sayName(self):
        return self.name
    
#Creamos dos personas y dos robots, la persona 1 tiene un robot azul y la persona 2 uno rojo


RobotA = Robot("Tom","Azul",120)
RobotB = Robot("Wall-e","Rojo",98)

Persona1 = Person("Luis","Happy",True,RobotA)
Persona2 = Person("Danu","Agressive",False,RobotB)

print("Programa para entender POO \n \n")
print(f"Hola soy la Persona1 y me llamo {Persona1.sayName()} y tengo un robot color {Persona1.robot.color} \n")
print(f"Hola soy la Persona2 y me llamo {Persona2.sayName()} y tengo un robot color {Persona2.robot.color}")


#Inheritance: behaviors and characteristics

class IndustrialRobot(Robot):
    def __init__ (self, name, color, weight):
        Robot.__init__(self,name,color,weight)

    def Suma(self,n1,n2):
        return n1+n2

RobotIndustrial = IndustrialRobot("KUKA","Orange",500)

print(f"El Robot Industrial se llama {RobotIndustrial.name} y suma {RobotIndustrial.Suma(1,3)}")