print("Grade Entry System")

grades = []
gradeCount = 0
totalPoints = 0
continueEntry = "yes"

while continueEntry != "no": # while: repeats the code as long as the condition is true; !: not equal to.
    grade = float(input("Add a grade: ")) # float: converts the input into a number that can include decimals.

    grades.append(grade) # append: adds the new grade to the end of the grades list. 
    gradeCount = gradeCount + 1
    totalPoints = totalPoints + grade

    continueEntry = input("Continue entering grades? (no to stop): ")

print("List of grades:", grades)
print("Total grades entered:", gradeCount)
print("Total points:", totalPoints)
