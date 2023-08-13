class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(Person):
    def __init__(self, first_name, last_name, teaching_subject):
        super().__init__(first_name, last_name)
        self.teaching_subject = teaching_subject

    def teach(self):
        print(f"{self.get_full_name()} is teaching {self.teaching_subject}")


class Student(Person):
    def __init__(self, first_name, last_name, student_id):
        super().__init__(first_name, last_name)
        self.student_id = student_id

    def study(self):
        print(f"{self.get_full_name()} is studying")


class Subject:
    def __init__(self, name):
        self.name = name


class Academy:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
        self.subjects = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)


math_teacher = Teacher("John", "Doe", "Mathematics")
physics_teacher = Teacher("Jane", "Smith", "Physics")

student1 = Student("Alice", "Johnson", "S123")
student2 = Student("Bob", "Williams", "S124")

math_subject = Subject("Mathematics")
physics_subject = Subject("Physics")

academy = Academy("Example Academy")
academy.add_teacher(math_teacher)
academy.add_teacher(physics_teacher)
academy.add_student(student1)
academy.add_student(student2)
academy.add_subject(math_subject)
academy.add_subject(physics_subject)

print(f"Teachers at {academy.name}:")
for teacher in academy.teachers:
    teacher.teach()

print(f"\nStudents at {academy.name}:")
for student in academy.students:
    student.study()