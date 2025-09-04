# Problem: Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), E (below 60).

user_score = int(input("enter student score: "))

if(user_score >= 101):
    print("Please enter valid student score!")
    exit()

if user_score < 60:
    grade = 'E'
elif user_score < 70:
    grade = 'D'
elif user_score < 80:
    grade = 'C'
elif user_score < 90:
    grade = 'B'
else:
    grade = 'A'

print(grade)