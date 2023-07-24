import csv
from validation import Grades, Names

class Student:
    last_name = Names(str.isalpha,
                       "Фамилия должна состоять только из букв.",
                       str.istitle,
                       "Первая буква должна быть заглавной.")    
    first_name = Names(str.isalpha,
                        "Имя должно состоять только из букв.",
                        str.istitle,
                        "Первая буква должна быть заглавной.")
    patronymic = Names(str.isalpha,
                        "Отчество должно состоять только из букв.",
                        str.istitle,
                        "Первая буква должна быть заглавной.")
    
    marks = Grades(2, 5)
    test_scores = Grades(0, 100)

    def __init__(self, last_name, first_name, patronymic):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic        

    def __str__(self):
        return (f'\n{"=" * 60}'
                f'\n{self._last_name} {self._first_name} {self._patronymic}'
                f'\nСредний балл (по всем предметам): {self.get_marks_average()}'
                f'\nСредние результаты тестов по предметам:'
                f'\n{self.averages_str()}'
                f'\n{"=" * 60}')

    def get_test_scores_average(self) -> dict[str, float]:
        result = {}
        for i_subj, i_scores in self.test_scores.items():
            result[i_subj] = round(sum(i_scores) / len(i_scores), 2)
        return result

    def get_marks_average(self) -> float:
        result = []
        for i_marks in self.marks.values():
            result.append(sum(i_marks) / len(i_marks))
        return round(sum(result) / len(result), 2)

    def averages_str(self) -> str:
        return '\n'.join([f'{i_key + ":":_<30}{i_val:<10}'
                          for i_key, i_val in self.get_test_scores_average().items()])