status=""
loginuser=input("Enter the user type :  ")
if(loginuser=="root"):
    status=input(" Enter the service Name :   ")
    if(status=="stopped"):
        status="start"
        print("******Congrats*****")
        print("service is {} now becasue you are the {} user".format(status, loginuser))
else:
    print("you don't have enough privilages")

