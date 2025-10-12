from classes.student import Student
from classes.mentor import Reviewer, Lecturer, Mentor

student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python']
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(student_1, 'Python', 10)
cool_mentor.rate_hw(student_1, 'Python', 10)
cool_mentor.rate_hw(student_1, 'Python', 10)
 
print(student_1.grades)

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
print(isinstance(lecturer, Mentor)) # True
print(isinstance(reviewer, Mentor)) # True
print(lecturer.courses_attached)    # []
print(reviewer.courses_attached)    # []