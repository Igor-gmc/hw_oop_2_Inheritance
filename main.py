from classes.student import Student
from classes.mentor import Reviewer, Lecturer, Mentor

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')
 
student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']
 
student.rate_lecture(lecturer, 'Python', 7)   # None
student.rate_lecture(lecturer, 'Java', 8)     # Ошибка
student.rate_lecture(lecturer, 'С++', 8)      # Ошибка
student.rate_lecture(reviewer, 'Python', 6)   # Ошибка

print(lecturer.grades)  # {'Python': 7}
print(lecturer.name, lecturer.surname)         # Преподаватель: Пётр Петров