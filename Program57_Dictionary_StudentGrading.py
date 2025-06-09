#Wap to


student_marks= {
    "st1": 92,
    "st2": 78,
    "st3": 56,
    "st4": 41,
    "st5": 99,
    "st6": 34,
    "st7": 12
}
print(student_marks)
# for key, value in student_marks.items():
#     if 91 <= value <= 100:
#         student_marks[key] = 'A+'
#     elif 81 <= value <= 90:
#         student_marks[key] = 'A'
#     elif 71 <= value <= 80:
#         student_marks[key] = 'B+'
#     elif 61 <= value <= 70:
#         student_marks[key] = 'B'
#     elif 51 <= value <= 60:
#         student_marks[key] = 'C'
#     elif 41 <= value <= 50:
#         student_marks[key] = 'D'
#     elif 31 <= value <= 40:
#         student_marks[key] = 'E'
#     else:
#         student_marks[key] = "Fail"
# print(student_marks)

#################### Approach 2 ###################
student_grades = {}
for student in student_marks:
    marks = student_marks[student]
    if 90 > marks:
        student_grades[student] = 'A+'
    elif 81 > marks:
        student_grades[student] = 'A'
    elif 71 > marks:
        student_grades[student] = 'B+'
    elif 61 > marks:
        student_grades[student] = 'B'
    elif 51 > marks:
        student_grades[student] = 'C'
    elif 41 > marks:
        student_grades[student] = 'D'
    elif 31 > marks:
        student_grades[student] = 'E'
    else:
        student_grades[student] = "Fail"
print(student_grades)
