from classes.student import Student
from classes.mentor import Reviewer, Lecturer

# Создаем объекты классов
lecturer_1 = Lecturer('Иван', 'Иванов')
lecturer_2 = Lecturer('Семен', 'Семенков')

reviewer_1 = Reviewer('Пётр', 'Петров')
reviewer_2 = Reviewer('Николай', 'Николаев')

student_1 = Student('Алена', 'Алехина', 'Ж')
student_2 = Student('Василий', 'Васильев', 'М')


# Вносим данные по курсам студента
student_1.courses_in_progress += ['Python', 'Java']
student_1.finished_courses += ['Введение в программирование']
student_2.courses_in_progress += ['C++', 'Java']
student_2.finished_courses += ['Введение в программирование', 'Python']

# Записываем курсы для лекеторов и проверяющих
lecturer_1.courses_attached += ['Python', 'Java']
reviewer_1.courses_attached += ['Python', 'C++']    # Проверку С++ менторы могут проводить по очереди, сначала один преподаватель
lecturer_2.courses_attached += ['C++', 'Java']
reviewer_2.courses_attached += ['Java', 'C++']      # а потом другой

# Выставляем оценки студенту 1
reviewer_1.rate_hw(student_1, 'Python', 10)  # None
reviewer_1.rate_hw(student_1, 'Python', 5)  # None
reviewer_2.rate_hw(student_1, 'Java', 8)  # None
reviewer_2.rate_hw(student_1, 'Java', 10)  # None

# Выставляем оценки студенту 2
reviewer_1.rate_hw(student_2, 'С++', 9)  # None
reviewer_2.rate_hw(student_2, 'Java', 8)  # None
reviewer_2.rate_hw(student_2, 'Java', 10)  # None
reviewer_2.rate_hw(student_2, 'С++', 7)  # None
 
# Выставляем оценки лектору
student_1.rate_lecture(lecturer_1, 'Python', 7)   # None
student_1.rate_lecture(lecturer_1, 'Java', 8)     # None
student_1.rate_lecture(lecturer_1, 'С++', 8)      # Ошибка

student_2.rate_lecture(lecturer_1, 'Java', 6)   # None
student_2.rate_lecture(lecturer_2, 'Java', 9)   # None
student_2.rate_lecture(lecturer_2, 'C++', 10)  # None
student_2.rate_lecture(lecturer_2, 'Python', 10)  # Ошибка

print('\n=======================================\n')
# Вывод информации по общим курсам лекторов
lecturer_1 == lecturer_2

print('\n=======================================\n')
for student in Student.all_students_list:
    print(student)                                          # Вывод информации по всем студентам
    # Расчитаем среднюю оценку по каждому курсу студента
    for course in student.courses_in_progress:
        print(student.average_grade_student_per_course(course))  # Вывод средней оценки по каждому курсу студента
    print('\n---------------------------------------\n')

print(student.average_grade_all_students_and_all_curses())  # Вывод средней оценки по всем студентам и всем курсам
print('\n=======================================\n')
#  Вывод лучшего студента по каждому курсу

print('\n=======================================\n')
#  Вывод отстающего студента по каждому курсу

print('\n=======================================\n')
print(lecturer_1)
print(lecturer_2)
print('\n=======================================\n')
print(reviewer_1)
print(reviewer_2)
print('\n=======================================\n')