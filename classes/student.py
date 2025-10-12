class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        # Проверяем, что lecturer - это объект класса Lecturer
        from classes.mentor import Lecturer
        # Проверяем, что курс есть в списке курсов студента и в списке курсов лектора
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            # Добавляем оценку в список оценок лектора по данному курсу в словарь
            lecturer.grades[course].append(grade) if course in lecturer.grades else lecturer.grades.setdefault(course, [grade])
            print('good') # для отладки
        else:
            print('Ошибка') # для отладки
            return 'Ошибка'
    
    def __str__(self):
        if self.grades:
            list_grades = []                                        # создаем пустой список для складирования всех оценок ото всех курсов
            for _, val_rgades in self.grades.items():               # проходим по всем курсам и их оценкам
                list_grades += val_rgades                           # добавляем оценки в общий список
            average_grade = sum(list_grades) / len(list_grades)     # вычисляем среднюю оценку
        else:
            average_grade = 'Оценок еще не было'                    # если оценок еще нет
            
        return  ( # для удобства чтения кода
                f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {average_grade}\n"
                f"Курсы в процессе изучения:{self.courses_in_progress}\n"
                f"Завершенные курсы:{self.finished_courses}\n"
        )