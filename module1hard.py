grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
print(students[::1])
#['Aaron', 'Bilbo', 'Johnny', 'Khendrik', 'Steve']
up_grades = sum(grades[0]) / len(grades[0])
print(up_grades)
up_grades = sum(grades[1]) / len(grades[1])
print(up_grades)
up_grades = sum(grades[2]) / len(grades[2])
print(up_grades)
up_grades = sum(grades[3]) / len(grades[3])
print(up_grades)
up_grades = sum(grades[4]) / len(grades[4])
print(up_grades)
up_grades = [4.0, 2.25, 4.0, 3.6666666666666665, 4.8 ]
my_students = dict(zip(students, up_grades))
print(my_students)