"""a. Professor Zak allows students to drop the four lowest scores on the ten 100-point quizzes she gives during the semester. 
Design an application that accepts a student name and 10 quiz scores. Output the student's name and total points for the student's six highest-scoring quizzes.

b. Modify the application in Exercise 3a so that the student's mean and median scores on the six best quizzes are displayed."""

grade_data = []
name = input("Please enter your name: ")

while len(grade_data) < 10:
    grade_input = input(f"Please enter your score on quiz {len(grade_data)+1}: ")
    if grade_input.isnumeric():
        score = int(grade_input)
        grade_data.append(score)
    else:
        print("Error: Invalid charcter.")

grade_data.sort()
six_highest_quizzes = grade_data[4:11]
count = 0

print(f"Name: {name}")
for x in six_highest_quizzes:
    count += 1
    print(f"Score {count}: {x}")