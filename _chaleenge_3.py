class Student:
    def __init__(self):
        self.__name = ""
        self.__rollNumber = ""

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getRollNumber(self):
        return self.__rollNumber

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber


student = Student()


student.setName("John Doe")
student.setRollNumber("2021001")

name = student.getName()
rollNumber = student.getRollNumber()


print("Name:", name)
print("Roll Number:", rollNumber)