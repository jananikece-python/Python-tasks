#task1: Pass or Fail
marks = int(input("Enter marks: "))

if marks >= 35:
    print("Pass")
else:
    print("Fail")

# task2:To Check voting Eligibility
Age = int(input("Enter age: "))

if Age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")

# task3: Shopping Discount
bill_amount= float(input("Enter shopping bill: "))

if bill_amount> 5000:
    discount = bill_amount * 0.10
else:
    discount = 0

final_amount = bill_amount - discount
print("Discount:", discount)
print("Final Amount:", final_amount)

#task4: Password Verification
stored_password = "accessyours"
password = input("Enter password: ")

if password == stored_password:
    print("Access Granted")
else:
    print("Wrong Password,Try again!")

#task5: Grade Assignment
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# task6: Simple Calculator
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Result:", num1 + num2)

elif operator == "-":
    print("Result:", num1 - num2)

elif operator == "*":
    print("Result:", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error! Division by zero is not allowed.")

else:
    print("Invalid operator!")

#task7: Electricity bill
units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = units * 3
else:
    bill = units * 5

print("Electricity Bill =", bill)

# task8:Ticket Fare
age = int(input("Enter Age: "))

if age < 5:
    fare = 0
elif age <= 12:
    fare = 50
else:
    fare = 100

print("Ticket Fare =", fare)

#task9:Loan Approval
salary = int(input("Enter your salary: "))

if salary > 30000:
    credit_score = int(input("Enter credit score: "))
    if credit_score > 700:
        print("Loan Approved")
    else:
        print("Loan Rejected: Credit Score is too low.")
else:
    print("Loan Rejected: Salary must be above 30,000.")

# task10: College Admission
academics = float(input("Enter academic percentage: "))

if academics > 60:
    entrance= int(input("Enter entrance exam score: "))
    if entrance > 70:
        print("Eligible for admission")
    else:
        print("Not Eligible : Entrance Score Low")
else:
    print("Not Eligible : Academic Marks Low")

# task11: Company Recruitment
degree = float(input("Enter degree percentage: "))

if degree > 65:
    aptitude = int(input("Enter aptitude score: "))
    if aptitude > 75:
        print("Selected")
    else:
        print("Rejected -  low Aptitude Score ")
else:
    print("Rejected -  low Degree Percentage ")

# task12: Scholarship
marks = float(input("Enter percentage: "))

if marks > 80:
    attendance = float(input("Enter attendance percentage: "))
    if attendance > 75:
        print("Scholarship Awarded")
    else:
        print("Scholarship Not Awarded - Attendance Low")
else:
    print("Scholarship Not Awarded - Marks Low")

# task13: ATM cash Withdrawal
balance = float(input("Enter account balance: "))
withdraw = float(input("Enter withdrawal amount: "))

if balance >= withdraw:
    pin = input("Enter PIN: ")
    if pin == "1212":
        balance=balance-withdraw
        print("Withdrawal Successful")
        print("Balance Amount in your Account:",balance)
    else:
        print("Incorrect PIN")
else:
    print("Insufficient Balance")

# task14: Secure Login
username = input("Enter username: ")

if username == "admin":
    password = input("Enter password: ")
    if password == "admin***":
        otp = input("Enter OTP: ")
        if otp == "1234":
            print("Login Successful")
        else:
            print("Invalid OTP")
    else:
        print("incorrect Password")
else:
    print("Invalid Username")

# task15: Hospital appointment
doctor_available = input("Is the doctor available? (yes/no): ")
slots_open = input("Are appointment slots available? (yes/no): ")

if doctor_available.lower() == "yes":
    if slots_open.lower() == "yes":
        print("Appointment Confirmed.")
    else:
        print("Appointment cannot be confirmed. No slots available.")
else:
    print("Appointment cannot be confirmed. Doctor is not available.")

# task16:Cybersecurity Lab Access
registered = input("Registered? (yes/no): ")

if registered.lower() == "yes":
    fees = input("Fees Paid? (yes/no): ")
    if fees.lower() == "yes":
        print("Access Granted")
    else:
        print(" Access Denied:Please Pay course Fees")
else:
    print("Access Denied:Registration Required")

# task17: Employee Bonus
experience = int(input("Enter years of experience: "))

if experience > 3:
    rating = float(input("Enter performance rating: "))
    if rating >= 8:
        print("Employee is Eligible for Bonus.")
    else:
        print("Not Eligible: Performance rating is below 8.")
else:
    print("Not Eligible: Experience must be more than 3 years." )

# task18: Online Exam Portal
hall_ticket = input("Hall Ticket Available? (yes/no): ")

if hall_ticket.lower() == "yes":
    fees = input("All Fees Cleared? (yes/no): ")
    if fees.lower() == "yes":
        print("Exam Access Granted.All the best!")
    else:
        print("Fees Pending-Access Denied")
else:
    print("Hall Ticket Not Available-Access Denied")

# task19: Hostel Room Allotment
selected = input("Are You Selected for Admission? (yes/no): ")

if selected.lower() == "yes":
    rooms = int(input("Available Rooms: "))
    if rooms > 0:
        print("Hostel Room Allotted")
    else:
        print("No Rooms Available")
else:
    print("Admission Not Confirmed")

#task20: Online Shopping offer
member = input("Are you a premium member? (yes/no): ")
amount = float(input("Enter purchase amount (₹): "))
discount = 0

if amount > 5000:
    if member.lower() == "yes":
        discount = amount * 20 / 100
        print("Discount: 20%")
    else:
        discount = amount * 10 / 100
        print("Discount: 10%")
else:
    print("No Discount")

final_amount = amount - discount

print("Final Amount =", final_amount)
