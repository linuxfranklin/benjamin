student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
#print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

tmp=0
for n in range(0, len(student_scores)):
  marks=(student_scores[n])
  if marks>tmp :
    tmp=marks
    
print(f"Highest mark is :  {tmp}")