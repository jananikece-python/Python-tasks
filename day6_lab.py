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



