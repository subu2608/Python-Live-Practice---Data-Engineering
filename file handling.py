'''
file=open("dummy.txt",'w')
file.write("Welcome")
file.write("\n")
file.write("This is your New Journey")
file.close()


file=open("dummy.txt",'r')
print(file.read())
file.close()


file=open("dummy.txt",'a')
file.write("Hello\n")
file.write("This is your New Journey\n")
file.close()

with open("dummy.txt",'r') as file:
    for l in file:
        print(l.strip())
'''


Name=input("Enter your name:")
Age=input("Enter your age:")
with open("details.txt",'a') as log:
    log.write("Name:"+Name+"\nAge:"+Age+"\n")

print("Your Details are saved")