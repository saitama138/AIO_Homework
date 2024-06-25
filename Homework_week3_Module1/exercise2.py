class Ward:
    def __init__(self, name):
        self.name = name
        self.person = []  # Biến thực thể
    
    def add_person(self, persons):
        self.person.append(persons)
    
    def describe(self):
        print(f"Ward - Name: {self.name}")
        for p in self.person:
            p.describe()
    
    def count_doctor(self):
        count = 0
        for p in self.person:
            if isinstance(p, Doctor):
                count += 1
        return count
    
    def sort_age(self):
        self.person.sort(key=lambda p: p.yob)

class Student(Ward):
    def __init__(self, name, yob, grade):
        super().__init__(name)
        self.yob = yob
        self.grade = grade
    
    def describe(self):
        print(f'Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}')

class Teacher(Ward):
    def __init__(self, name, yob, subject):
        super().__init__(name)
        self.yob = yob
        self.subject = subject

    def describe(self):
        print(f'Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}')
    
class Doctor(Ward):
    def __init__(self, name, yob, specialist):
        super().__init__(name)
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        print(f'Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}')

