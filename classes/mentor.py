from typing import List, Dict
from classes.student import Student


class Mentor:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.courses_attached: List[str] = []

    def rate_hw(self, student: Student, course: str, grade: int):
        if not (1 <= grade <= 10):
            print("Ошибка: недопустимая оценка (1–10)")
            return "Ошибка"

        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.grades.setdefault(course, []).append(grade)
        else:
            print("Ошибка: курс не найден или студент не привязан")
            return "Ошибка"


class Lecturer(Mentor):
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
        self.grades: Dict[str, List[int]] = {}

    def average_grade(self) -> float:
        """Средняя оценка лектора по всем курсам"""
        all_grades = [g for lst in self.grades.values() for g in lst]
        return round(sum(all_grades) / len(all_grades), 2) if all_grades else 0.0

    @staticmethod
    def average_lecturer_grade(lecturers: List["Lecturer"], course: str) -> float:
        """Средняя оценка лекторов по определённому курсу"""
        grades = []
        for l in lecturers:
            if course in l.grades:
                grades += l.grades[course]
        return round(sum(grades) / len(grades), 2) if grades else 0.0

    # --- Сравнение лекторов по средней оценке ---
    def __gt__(self, other: "Lecturer") -> bool:
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() > other.average_grade()

    def __lt__(self, other: "Lecturer") -> bool:
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __eq__(self, other: "Lecturer") -> bool:
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() == other.average_grade()

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {self.average_grade():.2f}\n"
        )


class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"
