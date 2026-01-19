# Student Result Management System (SRMS)

def calculate_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"

def student_result():
    print("=== Student Result Management System (SRMS) ===")

    name = input("Enter student name: ")

    score1 = int(input("Enter score for Subject 1: "))
    score2 = int(input("Enter score for Subject 2: "))
    score3 = int(input("Enter score for Subject 3: "))

    total = score1 + score2 + score3
    average = total / 3
    grade = calculate_grade(average)

    print("\n--- Student Result ---")
    print("Name:", name)
    print("Total Score:", total)
    print("Average Score:", average)
    print("Grade:", grade)

student_result()
