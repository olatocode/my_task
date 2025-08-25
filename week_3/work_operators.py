# comparison operator
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= 10)
print(a <= 25)


score = 75

print(score >= 50)
print(score <= 50)
print(score == 100)

# Assignment operator 
x = 10
print("inital value:", x)

x += 5
print("After x += 5:", x)

x -= 2
print("After x -= 2:", x)

x *= 3
print("After x *= 3:", x)

x /= 4
print("After x /= 4:", x)

x %= 3
print("After x %= 3:", x)

x = 4
x **= 2
print("After x **= 2:", x)

x //= 3
print("After x //= 3:", x)

# define variables
balance = 1000
deposit = 200
withdraw = 150

balance += deposit   
balance -= withdraw  

print("Updated Balance:", balance)  

# logical operators
x = 10
y = 20

print(x > 5 and y > 15)  
print(x < 5 or y > 15)   
print(not x == 10)

age = 17
score = 85
eligible = (age < 18) and (score > 80)
print("Scholarship Eligible:", eligible)  

age = 22
has_ticket = False

can_enter = (age >= 18) and (has_ticket or age < 25)

print("Access Granted:", can_enter)  