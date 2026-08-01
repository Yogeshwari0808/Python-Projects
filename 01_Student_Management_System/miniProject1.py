# Store the data of students

num_of_students = int(input("Enter the number of students"))

student_data = []

#-------- Insert data ---------

for i in range(num_of_students):
    print(f"Enter the data of student {i+1}")
    name = input("Name")
    roll_no = int(input("Roll Number"))
    marks = int(input("marks"))

    if marks >= 90:
        grades = "A+"
    elif marks >=80:
        grades = "A"
    elif marks>=70:
        grades= "B+"
    elif marks>= 60:
        grades="B"
    elif marks>=33:
        grades= "c"
    else :
        grades="fail"

    students = {
    "name" : name,
   "roll_no": roll_no,
   "marks": marks,
   "grades": grades  
} 
    student_data.append(students)

print("All student data:\n")

for s in student_data:
    print(f"{s['name']} - roll number:{s['roll_no']} - marks:{s['marks']} - grades:{s['grades']}  ")

print("\n students who are passed")    

for s in student_data:
    if s["marks"]>=33:
     print(f"{s['name']} - Marks: {s['marks']}")