# Импортируем Student для проверки типов в методе rate_hw.
# Это безопасно, т.к. Student не вызывает Mentor напрямую (нет циклического импорта).
from typing import List, Dict
from classes.student import Student


# ---------------------------------------------------------------------
# КЛАСС MENTOR — базовый (родительский)
# ---------------------------------------------------------------------
class Mentor:
    """
    Базовый класс для всех преподавателей (менторов).
    От него наследуются:
      - Lecturer (лекторы, которых оценивают студенты)
      - Reviewer (проверяющие, которые оценивают студентов)
    """

    def __init__(self, name: str, surname: str):
        """
        Атрибуты:
          name — имя преподавателя
          surname — фамилия преподавателя
          courses_attached — список курсов, которые он ведёт
        """
        self.name = name
        self.surname = surname
        self.courses_attached: List[str] = []

    # ---------------------------------------------------------
    # Метод выставления оценок студентам (переопределяется в Reviewer)
    # ---------------------------------------------------------
    def rate_hw(self, student: Student, course: str, grade: int):
        """
        Mentor может выставить студенту оценку за домашнюю работу.
        Работает только если:
          1. Студент является объектом класса Student
          2. Курс привязан и к ментору, и к студенту
          3. Оценка в диапазоне 1–10
        """

        # Проверяем диапазон оценки
        if not (1 <= grade <= 10):
            print("Ошибка: недопустимая оценка (1–10)")
            return "Ошибка"

        # Проверяем принадлежность типов и курсов
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            # Добавляем оценку в словарь оценок студента
            student.grades.setdefault(course, []).append(grade)
        else:
            # Если курс не совпадает или тип объекта не Student — возвращаем ошибку
            print("Ошибка: курс не найден или студент не привязан")
            return "Ошибка"


# ---------------------------------------------------------------------
# КЛАСС LECTURER — наследник Mentor
# ---------------------------------------------------------------------
class Lecturer(Mentor):
    """
    Лектор — преподаватель, который ведёт лекции и получает оценки от студентов.
    Наследует имя, фамилию и список курсов от Mentor.
    """

    def __init__(self, name: str, surname: str):
        # Вызываем конструктор родителя через super()
        super().__init__(name, surname)
        # Добавляем уникальное для Lecturer поле — оценки за лекции
        # Формат: {'Python': [8, 10], 'Java': [9]}
        self.grades: Dict[str, List[int]] = {}

    # ---------------------------------------------------------
    # Подсчёт средней оценки лектора
    # ---------------------------------------------------------
    def average_grade(self) -> float:
        """
        Возвращает среднюю оценку лектора по всем курсам.
        Если оценок нет — возвращает 0.0
        """
        # Объединяем все оценки со всех курсов в один список
        all_grades = [g for lst in self.grades.values() for g in lst]
        # Считаем среднее значение
        return round(sum(all_grades) / len(all_grades), 2) if all_grades else 0.0

    # ---------------------------------------------------------
    # Подсчёт средней оценки всех лекторов по заданному курсу
    # ---------------------------------------------------------
    @staticmethod
    def average_lecturer_grade(lecturers: List["Lecturer"], course: str) -> float:
        """
        Статический метод: считает среднюю оценку всех лекторов по определённому курсу.
        Используется для статистики.
        Пример вызова:
          Lecturer.average_lecturer_grade([lecturer_1, lecturer_2], 'Python')
        """
        grades = []
        for l in lecturers:
            if course in l.grades:
                grades += l.grades[course]
        return round(sum(grades) / len(grades), 2) if grades else 0.0

    # ---------------------------------------------------------
    # Переопределяем магические методы сравнения
    # ---------------------------------------------------------

    def __gt__(self, other: "Lecturer") -> bool:
        """
        Сравнение лекторов по средней оценке (больше чем >)
        """
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() > other.average_grade()

    def __lt__(self, other: "Lecturer") -> bool:
        """
        Сравнение лекторов по средней оценке (меньше чем <)
        """
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __eq__(self, other: "Lecturer") -> bool:
        """
        Сравнение лекторов по средней оценке (равны ли ==)
        """
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() == other.average_grade()

    # ---------------------------------------------------------
    # Форматированный вывод информации о лекторе
    # ---------------------------------------------------------
    def __str__(self):
        """
        При вызове print(lecturer) выводится читаемая информация:
        имя, фамилия и средняя оценка за лекции.
        """
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {self.average_grade():.2f}\n"
        )


# ---------------------------------------------------------------------
# КЛАСС REVIEWER — наследник Mentor
# ---------------------------------------------------------------------
class Reviewer(Mentor):
    """
    Reviewer — проверяющий преподаватель.
    Его задача — выставлять оценки студентам за домашние задания.
    Наследует всё поведение Mentor, но имеет свой __str__ для красивого вывода.
    """

    def __str__(self):
        """
        При выводе print(reviewer) показываем только имя и фамилию.
        """
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"
