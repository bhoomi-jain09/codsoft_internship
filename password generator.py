#password generator in python
#import necessary module 
import random
import string
#geting length of password
length=int(input("enter the desired length of the password="))
#define all possible characters:letter,digits,punctuation
character=string.ascii_letters + string.digits + string.punctuation
#generate password using random choices
password="".join(random.choices(character,k=length))
#display the password
print("your generated password is",password)


