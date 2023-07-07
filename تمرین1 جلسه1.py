import math
w=float(input("enter weight to kg):"))
h=float(input("enter height to meter):"))
BMI=(w/(h*h))
if(BMI<18.5):print("UNDERWEIGHT")
if(18.5<BMI<24.9):print("NORMAL")
if(25<BMI<29.9):print("OVERWEIGHT")
if(30<BMI<34.9):print("OBESE")
if(35<BMI<29.9):print("EXTREMEY OBESE")

