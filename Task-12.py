class Student:
    def __init__(self, name, surname, course, grades):
        self.name = name
        self.surname = surname
        self.course = course
        self.grades = grades

    def calculate_average_grade(self):
        total_grades = sum(self.grades)
        average_grade = total_grades / len(self.grades)
        return average_grade
