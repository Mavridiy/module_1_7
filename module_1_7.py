grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)   #преобразование в список
res = students.sort()       #сортировка списка по алфавиту
average_grade = [sum(grades[x]) / len(grades[x]) for x in range(len(grades))]#вычисление среднего балла
students_average_grade_dict = {students[y]: average_grade[y] for y in range(len(students))}   #объединение списков в словарь
print(students_average_grade_dict)