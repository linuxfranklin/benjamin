height=float(input("Enter your height:"))
weight=float(input ("Enter your weight:"))
bmi=weight/ (height**2)
bmi_rounded=round(bmi)

if bmi_rounded<18 :
    print(f"You are under Weight BMI={bmi_rounded}")
elif bmi_rounded<=22 :
    print(f"you have a normal weight BMI={bmi_rounded}")
elif bmi_rounded<=28 :
    print(f"you are slightly over weight BMI={bmi_rounded}")
elif bmi_rounded<=33 :
    print(f"you are obese BMI={bmi_rounded}")
else :
    print(f"you are clinically obese BMI={bmi_rounded}")