import math
name=str(input("enter student name:"))
family=str(input("enter family sudent:"))
a=float(input("enter first number:"))
b=float(input("enter second number:"))
c=float(input("enter thirth number:"))     
average=(a+b+c)/3
if average>=17:print("Great")
if 12<average<17:print("Normal")
if average<12:print("Fail")