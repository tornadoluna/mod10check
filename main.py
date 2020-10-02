code = input("Enter 12 digit code: ")
def checkDigit(upc): #this is the method that checks the check digit
    if ((((int(upc[10]) + int(upc[8]) + int(upc[6]) + int(upc[4]) + int(upc[2]) + int(upc[0])) * 3) + (int(upc[9]) + int(upc[7]) + int(upc[5]) + int(upc[3]) + int(upc[1])) % 10) + int(upc[11] == 10 )):
        print("mod10 digit is correct");
    else:
        print("mod10 digit is incorrect");
checkDigit(code)#calls the method on the data inputed by the user
def checkLoop(code):
    total = 0
    for i in range(10):
        if(code[i]%2 == 0):
            total = total + (int(code[i]) * 3)
        else:
            total = total + int(code[i])
    if(( total % 10) + code[11] == 10):
        print("mod10 digit is correct");
    else:
        print("mod10 digit is incorrect");
checkLoop(code)