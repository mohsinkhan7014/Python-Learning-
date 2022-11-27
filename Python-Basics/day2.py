portNumber=input("Enter the port which you want to check")
if(int(portNumber)>5000 and int(portNumber)<10000):
    print("Given Port Number is allowed")
else:
    print("Give is not in range 5000 t0 10000")