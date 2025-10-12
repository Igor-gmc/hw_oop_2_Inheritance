from turtle import st
from classes.student import Student
from classes.mentor import Reviewer, Lecturer, Mentor

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

# Вносим данные по курсам и оценкам для студента
student.courses_in_progress += ['Python', 'Git']
student.finished_courses += ['Введение в программирование']
student.finished_courses += ['Java']

lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']
reviewer.rate_hw(student, 'Python', 10)  # None
reviewer.rate_hw(student, 'Python', 9)   # None
reviewer.rate_hw(student, 'Python', 8)   # None
reviewer.rate_hw(student, 'Java', 9)     # None
reviewer.rate_hw(student, 'Java', 10)     # None
 
student.rate_lecture(lecturer, 'Python', 7)   # None
student.rate_lecture(lecturer, 'Java', 8)     # Ошибка
student.rate_lecture(lecturer, 'С++', 8)      # Ошибка
student.rate_lecture(reviewer, 'Python', 6)   # Ошибка

print('\n=======================================\n')
print(student)
print(lecturer)
print(reviewer)