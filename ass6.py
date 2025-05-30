digit=input("enter any single digit number (0-9):")
 
digits_in_english = ['zero','one','two','three','four','six','seven','eight','nine',]
if digit.isdigit() and 0 <= int(digit) <= 9:
    print("the digit is in english:",digits_in_english[int(digit)])
else:
    print("please enter a valid digit number (0-9).") 
                    

