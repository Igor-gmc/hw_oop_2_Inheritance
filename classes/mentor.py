from classes.student import Student

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:            # если такой курс уже есть в словаре оценок студента
                student.grades[course] += [grade]   # добавляем оценку в список оценок по этому курсу
            else:                                   # если такого курса еще нет в словаре оценок студента
                student.grades[course] = [grade]    # создаем новый ключ-курс и записываем в него список с первой оценкой
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self) -> str:
        list_grades = []                                    # создаем пустой список для складирования всех оценок ото всех курсов
        for _, val_grades in self.grades.items():           # проходим по всем курсам и их оценкам
            list_grades += val_grades                       # добавляем оценки в общий список
        print(list_grades)                                  # для отладки
        average_grade = sum(list_grades) / len(list_grades) if list_grades else 0       # вычисляем среднюю оценку
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade:.2f}\n'

    # Метод сравнения есть ли лекторов общие курсы
    def __eq__(self, other)->bool:
        # Проверяем что other это экземпляр класса Lecturer
        if not isinstance(other, Lecturer): 
            print('Ошибка. Сравнение возможно только между лекторами')  
            return False 
        # Проверяем есть ли у лекторов общие курсы
        common_courses = set(self.courses_attached) & set(other.courses_attached)
        if common_courses:
            print(f'Общие курсы у лекторов {self.name} {self.surname} и {other.name} {other.surname}: {common_courses}')
            return True
        else:
            print(f'У лекторов {self.name} {self.surname} и {other.name} {other.surname} нет общих курсов')
            return False
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self) -> str:
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'
