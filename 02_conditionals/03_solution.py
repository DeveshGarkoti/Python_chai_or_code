# Grade Calculator
student_score = int(input("Student Score in numbers "))

if student_score > 100:
  print("wrong assing")
  exit()

if student_score >= 90:
  print("Grade: A")
elif student_score >= 80:
  print("Grade: B")
elif student_score >= 70:
  print("Grade: C")
elif student_score >= 60:
  print("Grade: D")
else:
  print("Grade F")

