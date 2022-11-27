shellName=input("Enter the shell Name")
profile=""
if(shellName=="bash"):
    profile=".bashrc"
elif(shellName=="ksh"):
    profile=".kshrc"
else:
    profile="noshell"

print("shell name {} and profile name is {}".format(shellName,profile))