#easy
# 1. Function to print "Hello World"
def hello():
    print("Hello World")
hello()

# 2. Function to add two numbers
def add(a, b):
    return a + b
print(add(10, 5))

# 3. Function to subtract two numbers
def subtract(a, b):
    return a - b
print(subtract(10, 5))

# 4. Function to multiply two numbers
def multiply(a, b):
    return a * b
print(multiply(10, 5))

# 5. Function to divide two numbers
def divide(a, b):
    return a / b
print(divide(10, 5))

# 6. Function to find the square of a number
def square(n):
    return n ** 2
print(square(4))

# 7. Function to find the cube of a number
def cube(n):
    return n ** 3
print(cube(3))

# 8. Function to check whether a number is even or odd
def evenorodd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(evenorodd(7))

# 9. Function to find the largest of two numbers
def largest(a, b):
    if a > b:
        return a
    else:
        return b
print(largest(15, 20))

# 10. Function to calculate the area of a rectangle
def rectangle_area(length, width):
    return length * width
print(rectangle_area(8, 5))


#intermediate
# 1. Function to find the factorial of a number
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
print(factorial(5))

# 2. Function to check whether a number is prime
def is_prime(n):
    if n <= 1:
        return "Not Prime"
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"
print(is_prime(7))

# 3. Function to generate Fibonacci series
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
fibonacci(10)
print()

# 4. Function to reverse a string
def reverse_string(s):
    return s[::-1]
print(reverse_string("Python"))

# 5. Function to count vowels in a string
def count_vowels(s):
    count = 0
    vowels = "aeiouAEIOU"
    for ch in s:
        if ch in vowels:
            count += 1
    return count
print(count_vowels("Programming"))

# 6. Function to check whether a string is a palindrome
def palindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"
print(palindrome("madam"))

# 7. Function to find the second largest element in a list
def second_largest(lst):
    lst = list(set(lst))
    lst.sort()
    return lst[-2]
print(second_largest([10, 20, 30, 40, 50]))

# 8. Function to remove duplicates from a list
def remove_duplicates(lst):
    return list(set(lst))
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))

# 9. Function to count the frequency of characters in a string
def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq
print(char_frequency("hello"))

# 10. Function to find the sum of all elements in a list
def sum_list(lst):
    total = 0
    for i in lst:
        total += i
    return total
print(sum_list([10, 20, 30, 40, 50]))


#easy lambda
# 1. Lambda function to add two numbers
add = lambda a, b: a + b
print(add(10, 20))

# 2. Lambda function to find the square of a number
square = lambda n: n ** 2
print(square(5))

# 3. Lambda function to find the cube of a number
cube = lambda n: n ** 3
print(cube(4))

# 4. Lambda function to check whether a number is even
even = lambda n: n % 2 == 0
print(even(8))
print(even(7))

# 5. Lambda function to find the largest of two numbers
largest = lambda a, b: a if a > b else b
print(largest(15, 25))

#intermediate lambda
# 1.lambda to sort a list of tuples by age
people = [("John", 25), ("Alice", 20), ("Bob", 30)]
people.sort(key=lambda x: x[1])
print(people)


# 2.lambda to sort student records by marks
students = [("Arun", 85), ("Meena", 92), ("Kiran", 78)]
students.sort(key=lambda x: x[1])
print(students)


# 3.lambda to find the longest string in a list
words = ["apple", "banana", "grapes", "watermelon"]
longest = max(words, key=lambda x: len(x))
print(longest)


# 4.lambda to calculate a 10% discount
discount = lambda price: price - (price * 10 / 100)
print(discount(1000))


# 5.lambda to convert temperatures from Celsius to Fahrenheit
celsius_to_fahrenheit = lambda c: (c * 9/5) + 32
print(celsius_to_fahrenheit(25))

#easy map()
# 1.map() to find squares of numbers
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))
print(squares)

# 2.map() to convert names to uppercase
names = ["janani", "arun", "meena"]

uppercase_names = list(map(lambda x: x.upper(), names))
print(uppercase_names)

# 3.map() to add 10 to each element
numbers = [5, 10, 15, 20]

result = list(map(lambda x: x + 10, numbers))
print(result)

# 4.map() to multiply all elements by 2
numbers = [2, 4, 6, 8]

result = list(map(lambda x: x * 2, numbers))
print(result)

# 5.map() to find cube values
numbers = [1, 2, 3, 4, 5]

cube = list(map(lambda x: x ** 3, numbers))
print(cube)

#intermediate map()
# 1.Convert Celsius values to Fahrenheit using map()
celsius = [0, 20, 30, 40]

fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)

# 2.Calculate salary increments using map() (10% increment)
salaries = [20000, 30000, 40000, 50000]

incremented_salary = list(map(lambda s: s + (s * 10 / 100), salaries))
print(incremented_salary)

# 3.Find lengths of words in a list
words = ["Python", "Java", "HTML", "Programming"]

lengths = list(map(lambda word: len(word), words))
print(lengths)

# 4.Convert strings to lowercase
names = ["JANANI", "ARUN", "MEENA"]

lowercase_names = list(map(lambda name: name.lower(), names))
print(lowercase_names)

# 5.Add GST to product price (18% GST)
prices = [100, 250, 500, 1000]

gst_prices = list(map(lambda p: p + (p * 18 / 100), prices))
print(gst_prices)

#easy filter()
# 1. Filter even numbers from a list
numbers = [10, 15, 20, 25, 30, 35]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


# 2. Filter odd numbers from a list
numbers = [10, 15, 20, 25, 30, 35]

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)


# 3. Filter positive numbers
numbers = [-10, 20, -5, 30, 0, 15]

positive_numbers = list(filter(lambda x: x > 0, numbers))
print(positive_numbers)


# 4. Filter negative numbers
numbers = [-10, 20, -5, 30, 0, 15]

negative_numbers = list(filter(lambda x: x < 0, numbers))
print(negative_numbers)


# 5. Filter numbers greater than 50
numbers = [25, 45, 50, 60, 75, 90]

greater_than_50 = list(filter(lambda x: x > 50, numbers))
print(greater_than_50)

#intermediate filter()
# 1.Filter prime numbers
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

prime_numbers = list(filter(is_prime, numbers))
print(prime_numbers)


# 2.Filter students who scored above 75
students = [("Arun", 80), ("Meena", 92), ("Kiran", 70), ("Priya", 78)]

result = list(filter(lambda x: x[1] > 75, students))
print(result)


# 3.Filter names starting with 'A'
names = ["Arun", "Meena", "Ajay", "Priya", "Anu"]

result = list(filter(lambda x: x.startswith("A"), names))
print(result)


# 4.Filter products costing more than ₹1000
products = [("Laptop", 50000), ("Mouse", 800), ("Keyboard", 1200), ("Monitor", 15000)]

result = list(filter(lambda x: x[1] > 1000, products))
print(result)


# 5.Filter employees earning above ₹30,000
employees = [("Ravi", 25000), ("Kumar", 35000), ("Sita", 45000), ("John", 28000)]

result = list(filter(lambda x: x[1] > 30000, employees))

#easy recursion
# 1.Print numbers from 1 to 10 using recursion
def print(n):
    if n > 10:
        return
    print(n)
    print(n + 1)
print(1)

# 2.Print numbers from 10 to 1 using recursion
def print(n):
    if n < 1:
        return
    print(n)
    print(n - 1)
print(10)

# 3.Find the sum of first N natural numbers
def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)
print(sum_n(5))

# 4.Find the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))

# 5.Print a name N times using recursion
def print_name(name, n):
    if n == 0:
        return
    print(name)
    print_name(name, n - 1)
print_name("Janani", 5)
print(result)

#intermediate recursion
# 1.Fibonacci series using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

terms = 10
for i in range(terms):
    print(fibonacci(i), end=" ")
print()


# 2.Reverse a string using recursion
def reverse_string(s):
    if s == "":
        return ""
    return reverse_string(s[1:]) + s[0]

print(reverse_string("Python"))


# 3.Find GCD of two numbers using recursion
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(24, 36))


# 4.Count digits in a number using recursion
def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

print(count_digits(12345))


# 5. Check whether a string is a palindrome using recursion
def palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])


# Scenario based #
#Scenario 1: student result system
def result(marks):
    if marks >= 75:
        return "Distinction"
    elif marks >= 60:
        return "First Class"
    elif marks >= 50:
        return "Second Class"
    else:
        return "Fail"

marks = int(input("Enter marks: "))

print("Result:", result(marks))

#Scenario 2:Employee salary
def calculate_salary(salary):
    bonus = salary * 0.10
    total_salary = salary + bonus
    return total_salary

salary = float(input("Enter salary: "))

print("Salary after 10% bonus:", calculate_salary(salary))

#Scenario 3:Electricity bill
def electricity_bill(units):
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = units * 3
    else:
        bill = units * 5
    return bill

units = int(input("Enter units consumed: "))

print("Electricity Bill = ₹", electricity_bill(units))

#Scenario 4:Voting eligibility
def check_vote(age):
    if age >= 18:
        return "Eligible to Vote"
    else:
        return "Not Eligible to Vote"

age = int(input("Enter your age: "))

print(check_vote(age))

#Scenario 5:Shopping cart
def calculate_bill(amount):
    gst = amount * 0.18
    total = amount + gst
    return gst, total

amount = float(input("Enter bill amount: "))

gst, total = calculate_bill(amount)

print("GST = ₹", gst)
print("Total Bill = ₹", total)

#Scenario 6:Bank system
balance = 1000  # Initial balance

def deposit(amount):
    global balance
    balance += amount
    print("Deposited: ₹", amount)

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Withdrawn: ₹", amount)
    else:
        print("Insufficient Balance")

def check_balance():
    print("Current Balance: ₹", balance)

deposit_amount = float(input("Enter deposit amount: "))
deposit(deposit_amount)

withdraw_amount = float(input("Enter withdrawal amount: "))
withdraw(withdraw_amount)

check_balance()

#Scenario 7:Attendance system
def attendance_percentage(total_classes, attended_classes):
    percentage = (attended_classes / total_classes) * 100
    return percentage

total = int(input("Enter total number of classes: "))
attended = int(input("Enter number of classes attended: "))

print("Attendance Percentage =", attendance_percentage(total, attended), "%")

#Scenario 8:Online exam
def student_result(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "Fail"

    return total, percentage, grade

m1 = int(input("Enter mark 1: "))
m2 = int(input("Enter mark 2: "))
m3 = int(input("Enter mark 3: "))
m4 = int(input("Enter mark 4: "))
m5 = int(input("Enter mark 5: "))  

total, percentage, grade = student_result(m1, m2, m3, m4, m5)  #function call

print("Total Marks =", total)
print("Percentage =", percentage)
print("Grade =", grade)         


#Scenario 9:Library management
def calculate_fine(days_late):
    if days_late <= 5:
        fine = days_late * 2
    elif days_late <= 10:
        fine = days_late * 5
    else:
        fine = days_late * 10
    return fine

days = int(input("Enter number of late days: "))

print("Fine Amount = ₹", calculate_fine(days))


#Scenario 10:Movie ticket booking
def ticket_cost(seats):
    price_per_seat = 200
    total = seats * price_per_seat
    return total

seats = int(input("Enter number of seats booked: "))

print("Total Ticket Cost = ₹", ticket_cost(seats)

