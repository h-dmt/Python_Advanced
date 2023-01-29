"""
On the first line, you will receive the number of students – N. On the following N lines,
you will be receiving a student's name and grade.
For each student print all his/her grades and finally his/her average grade,
formatted to the second decimal point in the format:
"{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
"""

n = int(input())
all_grades = tuple(input().split() for _ in range(n))
students_grade = {}
for marks in all_grades:
    student, grade = marks
    if student not in students_grade:
        students_grade[student] = [float(grade)]
    else:
        students_grade[student].append(float(grade))

for student, grades in students_grade.items():

    avg = sum(grades) / len(grades)
    str_marks = ' '.join(map(lambda g: f"{g:.2f}", grades))

    print(f"{student} -> {str_marks} (avg: {avg:.2f})")
