class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        from classes.mentor import Lecturer
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            lecturer.grades[course] = grade
            print('good')
        else:
            print('Ошибка')
            return 'Ошибка'
    
    def __str__(self):
        if self.grades:
            list_grades = []
            for _, val_rgades in self.grades.items():
                list_grades += val_rgades
            average_grade = sum(list_grades) / len(list_grades)
        else:
            average_grade = 'Оценок еще не было'
            
        return  (
                f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {average_grade}\n"
                f"Курсы в процессе изучения:{self.courses_in_progress}\n"
                f"Завершенные курсы:{self.finished_courses}\n"
        )