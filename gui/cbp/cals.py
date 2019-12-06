print()
class Student:
    def __init__(self, name, cless, age):
        self.name = str(name)
        self.cless = str(cless)
        self.age = int(age)

    def present(self):
         return "Hello, my name is " + str(self.name) + \
          " i'm in class " + str(self.cless) + " and i'm " + \
           str(self.age) + " years old!"

    def changeage(self):
        return "Hello, my name is " + str(self.name) + \
         " i'm in class " + str(self.cless) + " and i'm " + \
          str(self.age + 1) + " years old!"

s1 = Student("Jerry", "S4Pta",13)
s2 = Student("Richard", "S5Nea",14)
s3 = Student("Gilberto", "S7Fia",18)
s4 = Student("Kendrick", "S5Ena",45)
s5 = Student("Jeremiah", "S2Ena",12)
s6 = Student("Francisco", "S6Pta",16)
s7 = Student("Filipao", "S8Crl",21)
s8 = Student("Rodrigo", "S5Fra",15)
s9 = Student("David", "S7Frb",18)
s10 = Student("Guilherme", "S3Lit",17)

print("Student : (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)")
nem = int(input())
print()
fu12 = [s1.present(), s2.present(), s3.present(), s4.present(), s5.present(), s6.present(), s7.present(), s8.present(), s9.present(), s10.present()]
print(fu12[nem-1])
print()
newage = [s1.changeage(), s2.changeage(), s3.changeage(), s4.changeage(), s5.changeage(), s6.changeage(), s7.changeage(), s8.changeage(), s9.changeage(), s10.changeage()]
print("Do you want to change their age? (Yes/No)")
chan = input()
print()
if (chan == "Yes"):
    print(newage[nem-1])
if (chan == "No"):
    print("K den")
