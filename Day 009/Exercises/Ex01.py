student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Nescoreille": 62,
}

student_grades = {}

for student, score in student_scores.items():
    grade = ""
    if score <= 70:
        grade = "Fail"
    elif score <= 80:
        grade = "Acceptable"
    elif score <= 90:
        grade = "Exceeds Expectations"
    else:
        grade = "Outstanding"

    student_grades[student] = grade


print(student_grades)
