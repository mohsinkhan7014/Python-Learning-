Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# declaring a var/item in python
Name="Mohsin"
last_Name =" Khan"
Roll_No = 123

Sem_Fee=40000.12
Blood_Group= O+
SyntaxError: invalid syntax
Blood_Group= "O+"

print("Name of the Student {}, {}".format(Name,last_Name))
Name of the Student Mohsin,  Khan
print("Roll Number : {}".format(Roll_No))
Roll Number : 123
print("Per Se, Fee {} amd Blood Group {}".format(Sem_Fee,Blood_Group))
Per Se, Fee 40000.12 amd Blood Group O+



##########Formating the output by \n and \t

print("Studnet Name :  {} {} \n Student Roll Number : {}\n Student Per Sem Fee :{}".format(Name,last_Name,Roll_No,Sem_Fee))
Studnet Name :  Mohsin  Khan 
 Student Roll Number : 123
 Student Per Sem Fee :40000.12



## taking input from keyboard
 
number1=input()
12
print(number1)
12
EmpName=print("Eneter the Emp Name {}".format(input())
              aRUN
              AS
              SAS
              
KeyboardInterrupt
print("Eneter a Emp Name :" input())
              
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("Eneter a Emp Name :" ,input())
              
Mohsin
Eneter a Emp Name : Mohsin
eName=input("Eneter the name of the Emp : ")
              
Eneter the name of the Emp : Mohsin Khan\
type(eName
     
KeyboardInterrupt
type(eName)
     
<class 'str'>
clear
     
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
print(eName)
     
Mohsin Khan\
******************
     
SyntaxError: invalid syntax
###############################################
     
































eName= input("Enter the name of the Employee")
     
Enter the name of the EmployeeMohsin Khan
\
eId=input("Enter the Emp- Id : ")
     
Enter the Emp- Id : 123
eAddress=input("Enter the Address : ")
     
Enter the Address : Ajam Market Station Road Makrana
print("Name : {}\n Emp-Id : {}\n Emp-Address : {}".format(eName,eId,eAddress))
     
Name : Mohsin Khan
 Emp-Id : 123
 Emp-Address : Ajam Market Station Road Makrana









######Typ-ecasting
     
number1="23"
     
type(number1)
     
<class 'str'>
### if add this number with string it will give an error
     
number1+2
     
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    number1+2
TypeError: can only concatenate str (not "int") to str
print(int(number1)+121)
     
144

Number=12
     
NumberToString=str(Number)
     
NumberToString
     
'12'
pie=3.124
     
addition=pie + 12
     
addition
     
15.124
type(addition)
     
<class 'float'>
# means if you are adding int into float/double then it will come as float/double
     





