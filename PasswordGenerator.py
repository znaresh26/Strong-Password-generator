#import the random Function
import random

#The Variable with all the UpperCase letters
UpperCase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#The Variable with all the LowerCase letters
LowerCase="abcdefghijklmnopqrstuvwxyz"

#The variable with special Characters
Special="!@#$%^&*"

#The variable With digits
Digits="0987654321"

#The variable with all types of characters
CompleteSet=UpperCase+LowerCase+Special+Digits

#Take the required size of password 
Size=int(input("Enter the length of Password : "))

#The function generates the random Strong password of the specified length
Password= "".join(random.choice(CompleteSet) for i in range(Size))

print("\nThe Required password of length %d is : "%Size+Password)
