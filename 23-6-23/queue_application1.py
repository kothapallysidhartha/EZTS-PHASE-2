student_grade=[]
student_grade.append((1,"AKA"))
student_grade.append((4,"ANK"))
print("yes")
print(student_grade)
student_grade.append((3,"sid"))
student_grade.append((2,"SRI"))
student_grade.sort(reverse=True )
print("priority wise sorted:\n")
print(student_grade)
print("\noriginal queue\n:")
while student_grade:
    print(student_grade.pop())
