from classes.student import Student

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self) -> str:
        list_grades = self.grades.values()
        average_grade = sum(list_grades) / len(list_grades) if list_grades else 0
        return f'Имя{self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade:.2f}\n'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self) -> str:
        return f'Имя{self.name}\nФамилия: {self.surname}\n'
