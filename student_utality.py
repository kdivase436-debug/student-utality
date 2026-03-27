name=input("enter student name=")
print("enter marks of 5 subjects:")
m1=float(input("subject 1:"))
m2=float(input("subject 2:"))
m3=float(input("subject 3:"))
m4=float(input("subject 4:"))
m5=float(input("subject 5:"))
total=m1+m2+m3+m4+m5
percentage=total/6
print("result")
print("name is:",name)
print("total marks:",total)
print("percentage",percentage)
if percentage>=90:
    grade="A+"
elif percentage>=75:
    grade="A"
elif percentage>=60:
    grade="B"
elif percentage>=50:
    grade="C"
else:
    grade="fail"
print("grade",grade)

