class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def aver(self):
        grades_list = sum(self.grades.values(), [])
        result = sum(grades_list)/len(grades_list)
        return result

    def __str__(self):
        courses_in_progress_string = ",".join(self.courses_in_progress)
        finished_courses_string = ",".join(self.finished_courses)
        result = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.aver()}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return result

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравнение некорректно')
            return
        return self.aver() < other.aver()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating.__round__(2)}'
        return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнение некорректно')
            return
        return self.average_rating < other.average_rating

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result


best_lecturer_1 = Lecturer('Дмитрий', 'Заводской')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Кирилл', 'Пугающий')
best_lecturer_2.courses_attached += ['Java']

cool_reviewer_1 = Reviewer('Владимир', 'Всевидящий')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['Java']

cool_reviewer_2 = Reviewer('Михаил', 'Зловещий')
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['Java']

student_1 = Student('Саня', 'Татарский', 'M')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Ваня', 'Веселый', 'M')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Введение в программирование']

student_1.rate_hw(best_lecturer_1, 'Python', 6)
student_1.rate_hw(best_lecturer_1, 'Python', 7)
student_1.rate_hw(best_lecturer_1, 'Python', 9)

student_1.rate_hw(best_lecturer_2, 'Python', 6)
student_1.rate_hw(best_lecturer_2, 'Python', 6)
student_1.rate_hw(best_lecturer_2, 'Python', 8)

student_1.rate_hw(best_lecturer_1, 'Python', 7)
student_1.rate_hw(best_lecturer_1, 'Python', 9)
student_1.rate_hw(best_lecturer_1, 'Python', 8)

student_2.rate_hw(best_lecturer_2, 'Java', 8)
student_2.rate_hw(best_lecturer_2, 'Java', 8)
student_2.rate_hw(best_lecturer_2, 'Java', 9)

cool_reviewer_1.rate_hw(student_1, 'Python', 7)
cool_reviewer_1.rate_hw(student_1, 'Python', 9)
cool_reviewer_1.rate_hw(student_1, 'Python', 8)

cool_reviewer_2.rate_hw(student_2, 'Java', 7)
cool_reviewer_2.rate_hw(student_2, 'Java', 8)
cool_reviewer_2.rate_hw(student_2, 'Java', 9)

print(f'Список студентов:\n\n{student_1}\n\n{student_2}')

print(f'Список лекторов:\n\n{best_lecturer_1}\n\n{best_lecturer_2}')

print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}')

print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} {best_lecturer_2.surname} = {best_lecturer_1 > best_lecturer_2}')

student_list = [student_1, student_2]
lecturer_list = [best_lecturer_1, best_lecturer_2]

def student_rating(student_list, course_name):
    sum_all = 0
    count_all=0
    for stud in student_list:
        if course_name in stud.courses_in_progress:
            sum_all += sum(stud.grades.get(course_name, []))
            count_all = len(stud.grades.get(course_name, []))
    average_for_all = sum_all / count_all
    return average_for_all

def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if course_name in lect.courses_attached:
            sum_all += sum(lect.grades.get(course_name, []))
            count_all = len(lect.grades.get(course_name, []))
    average_for_all = sum_all / count_all
    return average_for_all

print(f"Средняя оценка всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python').__round__(2)}")
print(f"Средняя оценка всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python').__round__(2)}")