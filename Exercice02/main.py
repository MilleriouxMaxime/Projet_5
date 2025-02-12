students = {
    "Alice": {"Mathematiques": 90, "Francais": 80, "Histoire": 95},
    "Bob": {"Mathematiques": 75, "Francais": 85, "Histoire": 70},
    "Charlie": {"Mathematiques": 88, "Francais": 92, "Histoire": 78},
}

student_name = input("Entrez le nom de l'étudiant : ")

if student_name not in students:
    print(f"L'étudiant {student_name} n'existe pas dans la liste.")
else:
    student = students[student_name]
    print(f"Notes de {student_name} :")
    for subject, grade in student.items():
        print(f"{subject} : {grade}")
    average_grade = sum(student.values()) / len(student)
    print(f"Moyenne : {average_grade:.2f}")
