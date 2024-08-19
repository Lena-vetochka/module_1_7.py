grades = [[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]]
students = {'Jonny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list(students)                # переводим множество в список
students = sorted(students)   # сортируем список
average_mark = {}
for a in range(len(students)): average_mark[students[a]] =  [sum(grades[a]) / len(grades[a])]
print(average_mark)


