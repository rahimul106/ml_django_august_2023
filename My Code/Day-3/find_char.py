#Check a character exists in a number or not?
#Take input from user
userInput = input('Input any thing: ')

status = userInput.isnumeric()

if status == True :
    print(userInput,"is a number, there have no character.")
else:
    print(userInput,"is not  a number, there have one or more characters.")