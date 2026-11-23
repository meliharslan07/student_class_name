class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, stu_id, gpa):
        super().__init__(name, age)
        self.stu_id = stu_id
        self.gpa = gpa
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def status(self):
        if self.get_average() >= 50:
            return "Passed"
        else:
            return "Failed"


class GradStudent(Student):
    def __init__(self, name, age, stu_id, gpa, thesis_topic):
        super().__init__(name, age, stu_id, gpa)
        self.thesis_topic = thesis_topic

    def show_thesis(self):
        print("Thesis:", self.thesis_topic)


s1 = Student("Melih", 21, "20232152", 3.2)
s1.add_grade(75)
s1.add_grade(85)
s1.add_grade(60)

s1.show_person()
print("ID:", s1.stu_id)
print("Average:", s1.get_average())
print("Status:", s1.status())

print()

g1 = GradStudent("Burak", 25, "20219988", 3.6, "Autonomous Drones")
g1.show_person()
g1.show_thesis()