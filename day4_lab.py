#using break
#task 1:print 1 to 100 stop at 50
for i in range(1,100):
    if i==51:
        break
    print(i)

#task 2:ask for password untill correct
correct_password= "pass321"

while True:
    password=input("Enter the password:")

    if password==correct_password:
         print("Access granted")
         break
    else:
         print("Incorrect password try again")

#task 3:search for name
names=("peter","john","george","hardy","stephen")
search= input("Enter the name to search:")
              
for name in names:
        if name==search:
             print("Name found")
             break
else:
    print("Name not found")

#using continue
#task 4:skip multiplies of 3
for i in range(1,21):
    if i%3==0:
        continue
    print(i)

#task 5:print only odd numbers
for i in range(1,51):
    if i%2==0:
        continue
    print(i)

#task 6:skip vowels
text=input("Enter a string:")
for ch in text:
    if ch.lower() in "aeiou":
        continue
    print(ch,end="")

#using pass
#task 7:create empty function
def my_function():
    pass
print("program executed successfully")

#task 8:create empty class
class student:
    pass
print("empty class created")

#task 9:create loop
for i in range(1,6):
    if i==3:
        pass
    else:
    print(i)
    
#task 10:armstrong number
num = int(input("Enter a number: "))

temp = num
sum = 0
digits = len(str(num))

while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** digits)
    temp = temp // 10

if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
