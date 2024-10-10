student_grades = {
    'Ram' : 85,
    'Sham' : 92,
    'Ojas' : 88,
    'Anay' : 79
}
highGrade = student_grades['Ram']
for grade in student_grades.values():
    if highGrade < grade:
        highGrade = grade
for stdName,grade in student_grades.items():
    if grade == highGrade:
        print(f"highest grade student is {stdName} with {highGrade} grade")
student_grades['Eve'] = 95
print(student_grades)

sorted_dic = dict(sorted(student_grades.items()))
print(sorted_dic)