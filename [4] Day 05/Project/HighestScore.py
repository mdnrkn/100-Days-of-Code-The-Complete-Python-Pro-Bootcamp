student_scores = [150, 180, 200, 170, 160, 190, 175, 185, 210, 195, 205, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score is: {highest_score}")