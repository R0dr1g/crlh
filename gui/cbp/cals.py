class Student:
    def __init__(self, name, cless, age):
        self.name = str(name)
        self.cless = str(cless)
        self.age = int(age)

    def present(self):
         print("Hello, my name is {}, i'm in class {} and i'm {} years old!") .\
        format(self.name, self.cless, self.age)

    def changeage(self):
        b
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

s1.present()
