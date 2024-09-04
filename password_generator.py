import random
print("Welcome In Password Generator")
numbers=['1','2','3','4','5','6','7','8','9','0']
alphabets=['a','b','c','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','J','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols=['!','@','#','$','%','^','&','*','(',')','+','-','*','/','{','}','>','<']
password=[]
n1=int(input("Enter how many numbers you want in your password:"))
n2=int(input("Enter how many alphabets you want in your password:"))
n3=int(input("Enter how many symbols you want in your password:"))

for i in range(0,n1):
    ch=random.choice(numbers)
    password+=ch
for i in range(0,n2):
    ch=random.choice(alphabets)
    password+=ch
for i in range(0,n1):
    ch=random.choice(symbols)
    password+=ch
random.shuffle(password)    
fpassword=""
for ch in password:
    fpassword+=ch
print("\n\nYour Required Password Will Be :")    
print(fpassword)    