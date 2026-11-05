# 1.
name = "Rahul"
age = 20 
print("Name:", name) 
print("Age next year:", age + 1)
# 2.
student_name = "Anu"
student_age = 21

student_course = "Python"
print(student_name) 
print(student_age)
print(student_course)
# 3.
price = 99.50

quantity = 3
total = price * quantity
print("Total:", total)
# 4.
x = 10 
y = 20 
total = x + y
print(total)
# 5.
first_name = "Arun"
last_name = "Kumar"
full_name = first_name + " " + last_name
print("Full name: " + full_name)
print("Name length:", len(full_name))


# 6. Actual Division
a = 15
b = 4
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Remainder:", a % b)


# 7. Comparison Operator
marks = 75
if marks == 75:
    print("Marks are 75")


# 8. Multiple Conditions
age = 20
if age > 18 and age < 25:
    print("Eligible")


# 9. Both Conditions True
a = 10
b = 20
result = a > b and a < b
print("Result:", result)


# 10. Power Operator
x = 10
y = 3
print(x ** y)


# 11. Age Checking
age = int(input("Enter your age: "))
if age >= 18:
    print("Adult")
else:
    print("Minor")


# 12. Addition of Two Numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print("Sum:", sum)


# 13. Temperature Checking
temperature = float(input("Enter temperature: "))
if temperature > 30:
    print("Hot")
else:
    print("Normal")


# 14. Area of Circle
radius = float(input("Enter radius: "))
area = 3.14 * radius * radius
print("Area:", area)


# 15. Grade Calculation
marks = 85
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")


# 16. Voting Eligibility
age = 17
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")


# 17. Even or Odd
number = 10
if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# 18. Login Checking
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")


# 19. Grade Calculation
marks = 65
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "F"

print(grade)


# 20. Positive, Negative or Zero
number = 0
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# 21. Adult or Senior Citizen
age = 25
if age >= 60:
    print("Senior Citizen")
elif age >= 18:
    print("Adult")
else:
    print("Minor")


# 22. Voting Eligibility with Name
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(name + " is eligible to vote")
else:
    print(name + " is not eligible to vote")


# 23. Discount Calculation
price = float(input("Enter product price: "))
discount = float(input("Enter discount percentage: "))

discount_amount = price * discount / 100
final_price = price - discount_amount

print("Final price:", final_price)


# 24. Even or Odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 25. Find Greater Number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is greater")
elif b > a:
    print(b, "is greater")
else:
    print("Both numbers are equal")


# 26. Calculate Age
year = int(input("Enter your birth year: "))
age = 2026 - year
print("Your age is:", age)


# 27. Divisible by 3, 5 or Both
num = 15

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both")
elif num % 3 == 0:
    print("Divisible by 3")
elif num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 3 or 5")


# 28. Exam Eligibility
marks = 82
attendance = 78

if marks >= 50 and attendance >= 75:
    print("Eligible for exam")
else:
    print("Not eligible")


# 29. Largest of Three Numbers
a = 10
b = 20
c = 30

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest:", largest)


# 30. Student Admission
username = input("Enter username: ")
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))

if username == "student" and age >= 18:
    if marks >= 50:
        print("Admission successful")
    elif marks >= 40:
        print("Admission pending")
    else:
        print("Admission rejected")
else:
    print("Invalid username or age")
username = input("Enter username: ")
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))

if username == "student" and age >= 18:
    if marks >= 50:
        print("Admission successful")
    elif marks >= 40:
        print("Admission pending")
    else:
        print("Admission rejected")
else:
    print("Admission rejected")
