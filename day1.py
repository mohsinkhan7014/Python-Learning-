Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
ls
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    ls
NameError: name 'ls' is not defined
print("OS Type : Window")
OS Type : Window
print("Size of Disk : 121")
Size of Disk : 121
print("Type of the Disk : NFS)
      
SyntaxError: unterminated string literal (detected at line 1)
clear
      
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
fstype='xfs'
      
fpart=' /dev/xvdb1'
      
fsize='120G'
      
print('File System Tupe is : ', fstype)
      
File System Tupe is :  xfs
print('Partiction Type is : '+ fstype +"\n"+ "Disk Size is " +fsize)
      
Partiction Type is : xfs
Disk Size is 120G

format = "Formating by \t"
      
print("data1\tData1\ndata2\tData2\nData3")
      
data1	Data1
data2	Data2
Data3
ename = " Mr Rajpal Kumar"
      
eid=345
      
epay=133545.35
      
print("Employee Name :\t",ename, "\nEmp Id :\t", eid, "\nEmp Sal :\t",epay)
      
Employee Name :	  Mr Rajpal Kumar 
Emp Id :	 345 
Emp Sal :	 133545.35
print("Emp Name : %s\n EMp Id : %d\n Emp Pay :%f%(ename,eid,epay))
      
SyntaxError: unterminated string literal (detected at line 1)
print("Emp Name : %s\n EMp Id : %d\n Emp Pay :%f%" (ename,eid,epay))
      
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print("Emp Name : %s\n EMp Id : %d\n Emp Pay :%f%" (ename,eid,epay))
TypeError: 'str' object is not callable
print("Emp Name : %s\n EMp Id : %d\n Emp Pay :%f"%(ename,eid,epay))
      
Emp Name :  Mr Rajpal Kumar
 EMp Id : 345
 Emp Pay :133545.350000
name = " Ankit"
      
empid=1212
      
epay=123423
      
print("name is : {}\n Employee Id is : {}\n Employ pay : {}".format(name,empid,epay))
      
name is :  Ankit
 Employee Id is : 1212
 Employ pay : 123423
name = "Mohsin"
      
type(name)
      
<class 'str'>
i=1000
      
type(i)
      
<class 'int'>
clear
      
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
A=10
      
B-100.12
      
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    B-100.12
NameError: name 'B' is not defined
B=100.12
      
C=A+B
      
type(C)
      
<class 'float'>
3**2
      
9
3**12
      
531441
45//5
      
9
X="100"
      
y=int(X)
      
y
      
100
### string ---> Float--
      
"10"+"!2"
      
'10!2'
print(input("Pleas en"))
      
Pleas en

empName=input("Enter the name of the Employ")
      
Enter the name of the EmployArun
emp
      
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    emp
NameError: name 'emp' is not defined
empName
      
'Arun'
empId=input("Enter the employee ID: ")
      
Enter the employee ID: 123
type(empId)
      
<class 'str'>
empName=input("Enter the name in STring")
      
Enter the name in STringMohsin
emppId=input("Enter the id in interger")
      
Enter the id in interger1212
emppId=int(emppId)
      
type(emppId)
      
<class 'int'>
epay=input("enter sal")
      
enter sal123.12
epay=float(epay)
      
type(epay)
      
<class 'float'>
XYZ=float(input("Enter in float"))
      
Enter in float12312
type(XYZ)
      
<class 'float'>
print("name is : {}\n Employee Id is : {}\n Employ pay : {}".format(empName,emppId,epay))
      
name is : Mohsin
 Employee Id is : 1212
 Employ pay : 123.12
python
      
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    python
NameError: name 'python' is not defined
