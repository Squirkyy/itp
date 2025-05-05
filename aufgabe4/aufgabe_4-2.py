class Student:
    next_id = 1

    def __init__(self, name, major):
        self.id = Student.next_id
        Student.next_id += 1
        self.name = name
        self.major = major
        self.grades = {} 

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def remove_grade(self, subject):
        if subject in self.grades:
            del self.grades[subject]

    def average_grade(self):
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

    def __str__(self):
        avg = self.average_grade()
        return f"Student: {self.name} (StudentId: {self.id}, Schnitt: {avg:.2f})"
    

def main():
    students = [
        Student("Anna Müller", "Informatik"),
        Student("Max Schulz", "Mathematik"),
        Student("Lisa König", "Biologie")
    ]

    students[0].add_grade("Mathe", 1.3)
    students[0].add_grade("Informatik", 1.0)

    students[1].add_grade("Mathe", 2.0)
    students[1].add_grade("Statistik", 2.3)

    students[2].add_grade("Biologie", 1.7)
    students[2].add_grade("Chemie", 2.0)

    students.sort(key = lambda s : s.average_grade())

    for student in students:
        print(student)
main()