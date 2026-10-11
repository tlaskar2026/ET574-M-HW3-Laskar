#List of three students named Jon, Kim and Lee
students = ["Jon", "Kim", "Lee"]
students.extend(["Sara", "Miko"])
# Changes Jon to John
students[0] = 'John'
#  Funtion to print 'Hi name' for each student in the list
def greet_students():
    for student in students:
        print("Hi", student)
    print("Total number of students:", len(students))
# Call the funtion
greet_students()