from classes.student import Student
from classes.mentor import Reviewer, Lecturer

# Создаем объекты классов
lecturer_1 = Lecturer('Иван', 'Иванов')
lecturer_2 = Lecturer('Семен', 'Семенков')

reviewer_1 = Reviewer('Пётр', 'Петров')
reviewer_2 = Reviewer('Николай', 'Николаев')

student_1 = Student('Алена', 'Алехина', 'Ж')
student_2 = Student('Василий', 'Васильев', 'М')

# Курсы студентов
student_1.courses_in_progress += ['Python', 'Java']
student_1.finished_courses += ['Введение в программирование']
student_2.courses_in_progress += ['C++', 'Java']
student_2.finished_courses += ['Введение в программирование', 'Python']

# Курсы лекторов и проверяющих
lecturer_1.courses_attached += ['Python', 'Java']
lecturer_2.courses_attached += ['C++', 'Java']
reviewer_1.courses_attached += ['Python', 'C++']
reviewer_2.courses_attached += ['Java', 'C++']

# Проверяющие оценивают студентов
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_2.rate_hw(student_1, 'Java', 8)
reviewer_2.rate_hw(student_1, 'Java', 10)

reviewer_1.rate_hw(student_2, 'C++', 9)
reviewer_2.rate_hw(student_2, 'Java', 10)
reviewer_2.rate_hw(student_2, 'Java', 10)
reviewer_2.rate_hw(student_2, 'C++', 7)

# Студенты оценивают лекторов
student_1.rate_lecture(lecturer_1, 'Python', 7)
student_1.rate_lecture(lecturer_1, 'Java', 8)
student_2.rate_lecture(lecturer_1, 'Java', 6)
student_2.rate_lecture(lecturer_2, 'Java', 9)
student_2.rate_lecture(lecturer_2, 'C++', 10)

# --- Тестирование функционала ---
print('\n=== Сравнение лекторов по средней оценке ===')
print(f"lecturer_1 > lecturer_2: {lecturer_1 > lecturer_2}")
print(f"lecturer_1 < lecturer_2: {lecturer_1 < lecturer_2}")
print(f"lecturer_1 == lecturer_2: {lecturer_1 == lecturer_2}")

print('\n=== Список студентов ===')
for student in Student.all_students_list:
    print(student)

print(f"\nСредняя оценка всех студентов: {Student.average_grade_all_students():.2f}")

print('\n=== Сравнение студентов ===')
print(f"student_1 > student_2: {student_1 > student_2}")
print(f"student_1 < student_2: {student_1 < student_2}")

print('\n=== Лекторы ===')
print(lecturer_1)
print(lecturer_2)

print('\n=== Проверяющие ===')
print(reviewer_1)
print(reviewer_2)
