line = "-" * 45
print(line)
print ("🟢List with strings🟢")

names = ["Bob", "Alex", "Kevin"]
names.append ("Joseph")

for name in sorted(names):
    print (names)

print (line)
print("🟢Lists with floats🟢")
measu = [-2.5, 1.1, 7.5, 14.6, 21.0, 19.2]
print(measu)
mean = sum(measu) / len(measu)
print ("The mean is:", mean)

print (line)
print("🟢List within lists🟢")
super_list = [[5,2,3],[4,1],[2,2,5,1]]
print(super_list)
print(super_list[1])

print(line)
grades = [["Shakira", 8, "D"], ["Melissa", 0, "C"], ["Shensi", 10, "A"]]
print(grades)
for student in grades:
    name = student [0]
    grade = student [1]
    group = student [2]
    print (f"*{name} from group {group} got a {grade}.")
    print(student)

print(line)
print("🟢Matrices🟢")
matrix = [[1,2,3], [4,5,6], [7,8,9]]

#print(rows)
for row in matrix:
    print("Row")
    print(row)
print("-" * 15)
for column in matrix:
    n1 = column [0]
    n2 = column [1]
    n3 = column [2]
    print("Column")
    print(column)
print(line)