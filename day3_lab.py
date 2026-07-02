#task 1:print name for loop
for i in range (5):
     print ("Janani")

#task 2 :numbers 1 to 20
for i in range (1,21):
     print (i)

#task 3 :numbers 20 to 1
for i in range (20,0,-1):
    print (i)

#task 4 :even numbers
for i in range (2,51,2):
    print (i)

#task 5 :odd numbers
for i in range (1,51,2):
    print (i)

#task 6 :sum of numbers
sum=0
for i in range (1,11):
    sum =sum + i
print("sum=",sum)

#task 7 :multiplication table
num =int(input("Enter a number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)
    
#task 8 :count letters
name = input("Enter name:")
count= len(name)
print("Number of letters=",count)

#task 9 : character in new line
word = input("Enter a word:")
for ch in word:
    print(ch)

#task 10 :number of vowels
word = input("Enter a word:")
count=0
for ch in word.lower():
    if ch in "aeiou":
        count +=1
print("number of vowels=",count)

#task 11 :cross pattern
n=5
for i in range (n):
    for j in range (n):
        if i==j or i+j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

#task 12 :right angle triangle
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
