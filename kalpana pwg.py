import random
import string
print("welcome to our Random Password Generator")
def my_function():
    length=int(input("Enter the length of password you want: "))
    lowerD=string.ascii_lowercase
    upperD=string.ascii_uppercase
    digitD=string.digits
    symbolsD=string.punctuation
    combine=lowerD+upperD+digitD+symbolsD
    combine+=combine
    x=random.sample(combine,length)
    password="".join(x)
    print(password)
    my_function()
my_function()
