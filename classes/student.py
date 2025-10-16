from __future__ import annotations
from typing import List, Dict


class Student:
    all_students_list: List["Student"] = []

    def __init__(self, name: str, surname: str, gender: str):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses: List[str] = []
        self.courses_in_progress: List[str] = []
        self.grades: Dict[str, List[int]] = {}
        Student.all_students_list.append(self)

    # Универсальная функция подсчёта среднего
    @staticmethod
    def calc_average(grades: Dict[str, List[int]]) -> float:
        all_grades = [g for grades_list in grades.values() for g in grades_list]
        return round(sum(all_grades) / len(all_grades), 2) if all_grades else 0.0

    def rate_lecture(self, lecturer: Lecturer, course: str, grade: int):
        from classes.mentor import Lecturer

        if not (1 <= grade <= 10):
            print("Ошибка: недопустимая оценка (должна быть от 1 до 10)")
            return "Ошибка"

        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            lecturer.grades.setdefault(course, []).append(grade)
        else:
            print("Ошибка: курс не найден или лектор не привязан")
            return "Ошибка"

    def average_grade(self) -> float:
        """Средняя оценка студента по всем курсам"""
        return Student.calc_average(self.grades)

    def __gt__(self, other: "Student") -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() > other.average_grade()

    def __lt__(self, other: "Student") -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {self.average_grade():.2f}\n"
            f"Курсы в процессе изучения: {', '.join(self.courses_in_progress) or '—'}\n"
            f"Завершенные курсы: {', '.join(self.finished_courses) or '—'}\n"
        )

    @staticmethod
    def average_grade_all_students() -> float:
        """Средняя оценка всех студентов по всем курсам"""
        grades = [g for s in Student.all_students_list for gl in s.grades.values() for g in gl]
        return round(sum(grades) / len(grades), 2) if grades else 0.0
