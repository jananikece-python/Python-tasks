#task1:temperature converter
c=float(input("Enter temp in celsius:"))
farenheit=(c*1.8)+32
print("Temperature in farenheit:",farenheit)

#task 2:simple interest calculator
principal=int(input("Enter principal amount:"))
rate=int(input("Enter the annual rate of interest:"))
time=int(input("Enter time in years:"))
SI=principal*rate*time/100
print("Simple interest:",SI)

#task 3:square and cube generator
n=int(input("Enter the whole number:"))
square=n**2
cube=n**3
print("Square value is:",square)
print("Cube value is:",cube)

#task 4:total minutes & seconds
hours=float(input("Enter the duration in hours:"))
minutes=hours*60
seconds=hours*3600
print("Total minutes:",minutes)
print("Total seconds:",seconds)

#task 5:average of three marks
Tamil=int(input("Enter Tamil marks:"))
English=int(input("Enter English marks:"))
Maths=int(input("Enter Maths marks:"))
Total=Tamil+English+Maths
Average=Total/3
print("Average score is:",Average)

#task 6:digits extractor
num=int(input("Enter 3 digit number:"))
first=num//100
second=(num//10)%10
third=num%10
print("First digit:",first)
print("Second digit:",second)
print("Third digit:",third)

#task 7:swap without a third variable using bitwise operators
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
a=a^b
b=a^b
a=a^b
print("a=",a)
print("b=",b)

#task 8:the atm cashier breakdown
amount=int(input("Enter amount:"))
five_hundred= amount//500
remaining= amount%500
hundred=remaining//100
print("500 notes:",five_hundred)
print("100 notes:",hundred)

#task 9:weeks and lefover days converter
Days=int(input("Enter total number of days:"))
Weeks=Days//7
Leftover_days=Days%7
print("Number of weeks:",Weeks)
print("Number of days left:",Leftover_days)

#task 10:reverse a 2-digit number mathematically
number=int(input("Enter 2-digit number:"))
last_digit=number%10
first_digit=number//10
reverse=(last_digit*10)+first_digit
print("Reversed number=",reverse)
