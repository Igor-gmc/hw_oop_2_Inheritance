class Student:
    all_students_list = []                      # Список всех студентов

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.all_students_list.append(self)   # Добавляем нового студента в список всех студентов

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
        
    def average_grade_all_students_and_all_curses(self):
        list_grades_all_students = []
        for student in Student.all_students_list:           # проходим по всем студентам в списке всех студентов
            for _, val_grades in student.grades.items():    # проходим по всем курсам и их оценкам
                list_grades_all_students += val_grades      # добавляем оценки в общий список
        average_grade = sum(list_grades_all_students) / len(list_grades_all_students) if list_grades_all_students else 0   # вычисляем среднюю оценку
        return f'Средняя оценка за домашние задания всех студентов: {average_grade:.2f}'
    
    def average_grade_student_per_course(self, course) -> str:
        if course in self.grades:
            list_grades = self.grades[course]                       # получаем список оценок по заданному курсу
            average_grade = sum(list_grades) / len(list_grades)     # вычисляем среднюю оценку
            return f'Средняя оценка за домашние задания по курсу {course}: {average_grade:.2f}'
        else:
            return f'По курсу {course} еще нет оценок'
        
    # используем для подсчета средней оценки одного студента по выбранному курсу
    def avg_student_per_course(self, course) -> float:
        list_grades = self.grades.get(course, None)
        if not list_grades:     # Проверяем есть ли по курсу оценки
            return 0.0          # Если оценок нет
        else:
            return sum(list_grades) / len(list_grades) # Возвращаем средню оценку по выбранному курсу
        
    def __gt__(self, other) -> bool:
        # Проверим есть ли сравниваемый студент в списке
        if not isinstance(other, Student):
            print(f'Такого студента нет: {other}')
            return False
        # Проверим наличие пересекающихся курсов у сравниваемых студентов
        common_courses = set(self.courses_in_progress) & set(other.courses_in_progress)
        if not common_courses:
            print(f'У студентов {self.name} и {other.name} нет общих курсов для сравнения')
            return False
        # Считаем среднюю оценку по найденным курсам у каждого студента
        total_grades_self_all_courses, total_grades_other_all_courses = 0, 0
        for crs in common_courses:
            # считаем среднюю оценку по итерироемому курсу
            avg_self = self.avg_student_per_course(crs)     # для первого студента
            avg_other = other.avg_student_per_course(crs)   # для второго студента
            # для отладки
            # print(f'Курс: {crs}')
            # print(f'Студент {self.name} {self.surname}, средняя оценка за предмет {avg_self}')
            # print(f'Студент {other.name} {other.surname}, средняя оценка за предмет {avg_other}')
            total_grades_self_all_courses += avg_self       # суммируем средние оценки для всех курсов первому студенту
            total_grades_other_all_courses += avg_other     # суммируем средние оценки для второго студента
        # считаем средние оценки по всем пересекающимся курасам выбранных студентов
        self_avg = total_grades_self_all_courses / len(common_courses)
        other_avg = total_grades_other_all_courses / len(common_courses)
        # выводим информацию по результатам вычислений
        if self_avg > other_avg:
            print(f'True - Средний бал за все курсы {self.name} ={avg_self} > {other.name} ={avg_other}')
            return True
        else:
            print(f'False - Средний бал за все курсы {self.name} ={avg_self} <= {other.name} ={avg_other}')
            return False
    
    def __lt__(self, other) -> bool:
        """Сравнение студентов по средней оценке по всем курсам (меньше чем <)"""

        # Проверяем, что сравниваем действительно студентов
        if not isinstance(other, Student):
            print(f'Ошибка: {other} не является студентом')
            return False

        # Собираем все оценки и считаем среднюю по всем курсам
        total_list_grade_self, total_list_grade_other = [], []

        # Оценки первого студента
        for val_grades in self.grades.values():
            total_list_grade_self += val_grades

        average_grade_self = (
            sum(total_list_grade_self) / len(total_list_grade_self)
            if total_list_grade_self else 0
        )

        # Оценки второго студента
        for val_grades in other.grades.values():
            total_list_grade_other += val_grades

        average_grade_other = (
            sum(total_list_grade_other) / len(total_list_grade_other)
            if total_list_grade_other else 0
        )

        # Сравнение средних баллов
        if average_grade_self < average_grade_other:
            print(
                f"True - Средний балл за все курсы {self.name} = {average_grade_self:.2f} "
                f"< {other.name} = {average_grade_other:.2f}"
            )
            return True
        else:
            print(
                f"False - Средний балл за все курсы {self.name} = {average_grade_self:.2f} "
                f">= {other.name} = {average_grade_other:.2f}"
            )
            return False

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