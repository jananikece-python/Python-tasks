'''#list tasks
#1.create a list and print even numbers
numbers=[1,2,3,4,5,6,7,8,9,10]
print("Even numbers are:")
for num in numbers:
    if num%2==0:
        print(num)

#2.to find largest and smallest
numbers=[2,8,13,52,36,23,12]

largest=max(numbers)
smallest=min(numbers)
print("Largest number is:",largest)
print("Smallest number is:",smallest)

#3.calculate sum and average
numbers=[1,2,3,4,5]

total=sum(numbers)
average=total/len(numbers)
print("Sum=",total)
print("Average:",average)

#4.to remove duplicate elements
numbers=[1,2,3,4,5,2,4,6,7]

verified_list=list(set(numbers))
print("list after removing duplicates:",verified_list)

#5.to find second largest number
numbers=[11,16,43,26,54,82,63]

numbers=list(set(numbers))
numbers.sort()
second_largest=numbers[-2]
print("second largest number is:",second_largest)

#6.reverse a list
numbers=[1,2,3,4,5]
reversed_list=numbers[::-1]
print(reversed_list)

#7.merge two list
list1 = [5, 2, 8]
list2 = [1, 9, 3]
merged_list = list1 + list2
merged_list.sort()

print("Merged and Sorted List:", merged_list)

#8.count the element no.of time occurs
numbers = [2,5,7,3,5,7,2,8]

element = int(input("Enter the element to count: "))
count = numbers.count(element)

print("The element", element, "appears", count, "times in a list")

#9.even and odd in separate list
numbers = [10, 15, 22, 33, 40, 55, 60]
even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)

#10.search for student name
students = ["Arun", "Riya", "Priya", "Keerthana", "Ambreena"]

name = input("Enter the student name to search: ")

if name in students:
    print(name, "is found in the list.")
else:
    print(name, "is not found in the list.")'''

#Tuple tasks
#1.create a tuple
subjects = ("Tamil","English", "Maths", "Science", "Social")

for subject in subjects:
    print(subject)

#2.find the length
subjects = ("Tamil","English", "Maths", "Science", "Social")

length = len(subjects)

print("Length of the tuple:", length)

#3.count the occurrence of element
numbers = (1,4,2,5,7,3,6,4,8,5)

value = int(input("Enter the value to count: "))
count = numbers.count(value)

print("The value", value, "appears", count, "times.")

#4.to find index of element
numbers = (10, 20, 30, 40, 50)

element = int(input("Enter the number to find: "))

if element in numbers:
    print("Index of", element, "is", numbers.index(element))
else:
    print(element, "is not found in the tuple.")

#5.convert tuple into list and add a element
numbers = (10,20,30,40,50)

num_list = list(numbers)
num_list.append(60)

print("Updated List:", num_list)

#6.to find min and max value
numbers = (15,8,23,42,5,19)

maximum = max(numbers)
minimum = min(numbers)

print("Maximum value:", maximum)
print("Minimum value:", minimum)

#7.concatenate two tuple
tuple1 = (10,20,30)
tuple2 = (40,50,60)

result = tuple1 + tuple2

print("Concatenated Tuple:", result)

#8.to check an element exist
numbers = (11,12,13,14,15)

element = int(input("Enter the number to search: "))

if element in numbers:
    print(element, "exists in the tuple.")
else:
    print(element, "does not exist in the tuple.")

#9.convert list into tuple and calculate average
marks = [75, 80, 90, 85, 70]

marks_tuple = tuple(marks)

average = sum(marks_tuple) / len(marks_tuple)

print("Tuple:", marks_tuple)
print("Average Marks:", average)

#10.to find first,last and middle value
numbers = (12,23,46,32,55)

first = numbers[0]
middle = numbers[len(numbers) // 2]
last = numbers[-1]

print("First element:", first)
print("Middle element:", middle)
print("Last element:", last)

#set tasks
#union,intersection,symmetric,difference
a={1,2,3,4,5}
b={3,4,5,6,7}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

#remove duplicates using set
A={1,2,3,4,5,4,6,5,7}

new_A=list(set(A))
print("original set:",A)
print("list after removing duplicates:",new_A)

#subset,superset
a={1,2,3}
b={1,2,3,4,5}

print(a.issubset(b))
print(b.issubset(a))

print(a.issuperset(b))
print(b.issuperset(a))

#add,remove
a={10,12,15,19,16,14}

a.add(13)
print(a)
a.remove(19)
print(a)

#find common students using set
classA = {"Ambreena", "Brindha", "Chitra", "Divya"}

classB = {"Chitra", "Divya", "Elavarasi", "Gayathiri"}

common_students = classA.intersection(classB)
print("Common students:", common_students)

#disjoint
set1 = {1, 2, 3, 4}
set2 = {5, 6, 7, 8}

if set1.isdisjoint(set2):
    print("The sets are disjoint.")
else:
    print("The sets are not disjoint.")

#Dictionary
#1.dictionary containing student details
student = {
    "Name": "Priya",
    "Age": 20,
    "Class": "B.Sc Computer Science",
    "Roll No":26
}

print(student)

student["Department"]="Computer Science" #2.add a new key-value
print(student)

student["Age"]=19  #3.update value of existing key
print(student)

del student["Class"]  #4.delete a key
print(student)

print(student.keys()) #5.print all keys

print(student.values()) #6.print all values

if "Age" in student:
    print("key exists")
else:
    print("key does not exist") #7.to find whether a key exist

#8.count the frequency
text = "hello"
frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print(frequency)

#9.find the student with high mark
marks = {
    "Ananya": 85,
    "Brindha": 92,
    "Chaiyathra": 78,
    "Divya": 95
}
top_student = max(marks, key=marks.get)

print("Student with the highest mark:", top_student)
print("Highest mark:", marks[top_student])

#10.merge two dictionaries
detail_1 = {
    "Name": "Rithu",
    "Age": 19
}
detail_2 = {
    "Class": "B.A",
    "Department": "English"
}

detail_1.update(detail_2)

print(detail_1)

#scenario based system

#list

#1.Shopping cart system
cart = []

cart.append("Milk")
cart.append("Bread")
cart.append("Eggs")

print("After adding products:")
print(cart)

cart.remove("Bread")

print("After removing Bread:")
print(cart)

#2.Student attendance list
attendance = ["Arun", "Priya", "Karthik", "Meena", "Rahul"]

student = input("Enter the student name to search: ")

if student in attendance:
    print(student, "is present.")
else:
    print(student, "is absent.")

#tuple

#3.store weekdays on a tuple
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"

num = int(input("Enter a number (1-7): "))

if 1 <= num <= 7:
    print("Day:", weekdays[num - 1])
else:
    print("Invalid input! Please enter a number between 1 and 7.")

#4.GPS coordinates
gps = (13.0827, 80.2707)

print("Latitude:", gps[0])
print("Longitude:", gps[1])

#set

#5.website visit tracker
visitors = set()

visitors.add("V101")
visitors.add("V102")
visitors.add("V103")
visitors.add("V101")

print("Unique Visitor IDs:")
for visitor in visitors:
    print(visitor)

#6.common courses enrolled
student1 = {"Python", "Java", "C++", "HTML"}
student2 = {"Python", "HTML", "JavaScript", "SQL"}

common_courses = student1.intersection(student2)

print("Common Courses:", common_courses)

#dictionary

#7.Employee database
employees = {
    101: {"Name": "Arun", "Department": "HR", "Salary": 35000},
    102: {"Name": "Priya", "Department": "Finance", "Salary": 45000},
    103: {"Name": "Karthik", "Department": "IT", "Salary": 50000}
}

for emp_id, details in employees.items():
    print("Employee ID:", emp_id)
    print("Name:", details["Name"])
    print("Department:", details["Department"])
    print("Salary:", details["Salary"])
    print()

#8.contact book
contacts = {
    "Arun": "98765432xx",
    "Meena": "98765012xx"
}

print("Contact Book:")
for name, phone in contacts.items():
    print(name, "->", phone)

#9.student mark management
students = {
    "Arun": 85,
    "Priya": 92,
    "Karthik": 78,
    "Meena": 88
}
print("Student Marks:")
for name, mark in students.items():
    print(name, ":", mark)

topper = max(students, key=students.get) #find topper
print("\nTopper:", topper)
print("Mark:", students[topper])

students["Karthik"] = 90

print("\nAfter Updating Marks:")  #update marks
for name, mark in students.items():
    print(name, ":", mark)

#10.library system
    library = {
    101: "Python Programming",
    102: "Data Structures",
    103: "Computer Networks",
    104: "Database Management"
}

book_id = int(input("Enter Book ID: "))

if book_id in library:
    print("Book Name:", library[book_id])
else:
    print("Book ID not found.")

#Challenge tasks
    
#1.convert list-tuple-set-dictionary
# List
fruits = ["Apple", "Banana", "Mango", "Orange"]

# List to Tuple
t = tuple(fruits)
print("Tuple:", t)

# Tuple to Set
s = set(t)
print("Set:", s)

# Set to Dictionary
d = {}
for item in s:
    d[item] = len(item)

print("Dictionary:", d)

#2.duplicate elements in a list using dictionary
numbers = [10, 20, 30, 20, 40, 10, 50, 20]

count = {}

for num in numbers:
    count[num] = count.get(num, 0) + 1

print("Duplicate Elements:")
for key, value in count.items():
    if value > 1:
        print(key)

#3.frequency of each word
sentence = input("Enter a sentence: ")

words = sentence.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word Frequency:")
for word, count in frequency.items():
    print(word, ":", count)

#4.common elements b/w two lists using set
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

common = set(list1).intersection(set(list2))

print("Common Elements:", common)

#5.student management system using list,tuple,set,dictionary
students = ["Anu", "Bala", "Charan"]          # List
subjects = ("Python", "Java", "HTML")         # Tuple
clubs = {"Sports", "Music", "NSS"}            # Set

marks = {
    "Anu": 90,
    "Bala": 85,
    "Charan": 95
}                                             # Dictionary

print("Students:", students)
print("Subjects:", subjects)
print("Clubs:", clubs)

print("\nStudent Marks:")
for name, mark in marks.items():
    print(name, ":", mark)




