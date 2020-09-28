scores = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for score in scores:
    print("The score is: ", score)

    if score >= 75:
        grade = "First"
    elif 70 <= score < 75:
        grade = "Upper Second"
    elif 60 <= score < 70:
        grade = "Second"
    elif 50 <= score < 60:
        grade = "Third"
    elif 45 <= score < 50:
        grade = 'F1 Supp'
    elif 40 <= score < 45:
        grade = 'F2'
    elif score < 40:
        grade = 'F3'
    else:
        grade = 'unknown'

    print('The grade is: ', grade)
