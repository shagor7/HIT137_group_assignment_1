#validate user input for number of students
while True:
    try:
        students_num = int(input("How many Students? "))
        if students_num > 0:
            break
        else:
            print("Invalid input. Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid integer!")
names = []
scores = []

for i in range(1, students_num+1):
    #validate user input for students' names and scores
    while True:
            name = input(f"Students {i} name: ").strip()
            if name == "":
                print("Invalid input. Name cannot be empty.")
            elif name.isdigit():
                print("Invalid input. Name cannot be a number.")
            else:
                break      
        
    while True:
        try:
            score = int(input(f"{name}'s score: "))
            if 0 <= score <= 100:
                break
            else:
                print("Invalid input. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer!")
    names.append(name)
    scores.append(score)

#grade calculation and output
for i in range(students_num):
    score = scores[i]

    if score >= 85:
        grade = "HD"
    elif score >= 75:
        grade = "D"
    elif score >= 65:
        grade = "C"
    elif score >= 50:
        grade = "P"
    else:
        grade = "F"
    print(f"{names[i]}: {score} ({grade})")

# Calculate average, highest, and lowest scores
average = sum(scores)/students_num
highest_score = max(scores)
lowest_score = min(scores)

# Find corresponding names
highest_name = names[scores.index(highest_score)]
lowest_name = names[scores.index(lowest_score)]

#output
print(f"Average score {average:.2f}")
print(f"Highest score {highest_name}  ({highest_score})")
print(f"Lowest score {lowest_name} ({lowest_score})")