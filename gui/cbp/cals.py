class Student:
    def __init__(self, name, class, age):
        self.name = str(name)
        self.calss = str(class)
        self.age = int(age)

    def present(self):
        presentation = ("Hello, my name is {}, i'm in class {} and i'm {} years old!") .\
            format(self.name, self.class, self.age)
        return str(presentation)

    def changeage(self):
        b
s1 = Student("Jerry", S4Pta,13)
s2 = Student("Richard", S5Nea,14)
s3 = Student("Gilberto", S7Fia,18)
s4 = Student("Kendrick", S5Ena,)
s5 = Student("Jeremiah", S2Ena)
s6 = Student("Francisco", S6Pta)
s7 = Student("Filipao", S8Crl)
s8 = Student("Rodrigo", S5Fra)
s9 = Student("David", S7Frb)
s10 = Student("Guilherme", S3Lit)

s1.present()
