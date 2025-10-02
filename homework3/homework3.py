# File: homwork3.py

# ---Print Fuctions---
# --Say Goodbye--
def say_goodbye(name):
    print("Goodbye,", name)
# say_goodbye("Teo")

# --Area of a Circle--
def area_circle(r):
    return 3.14*r**2
# print(area_circle(10))

# ---Return Functions---
# --Subtract, Multiply and Divide--
def subtract(a,b):
    return a - b
# print(subtract(6,2))

def multiply(a,b):
    return a*b
# print(multiply(5,4))

def divide(a,b):
    return a/b
# print(divide(10,2))

# ---Conditionals---
# --What Should I Wear?--
def temperature(list):
    return min(list), max(list)
# print(temperature([58,62,49,75,55,60,82,73]))

# --Check if it's the Weekend--
def is_weekend(num):
    if num==6 or num==7:
        return True
    else:
        return False
# print(is_weekend(6))

# --Fuel Efficiency Calculator--
def fuel_efficiency(a,b):
    efficiency=a/b 
    print(efficiency, "mpg")
# fuel_efficiency(80,4.5)

# --Secret Code--
def code(num): # doesn't work for negative numbers (or numbers that end in zero really cause you just lose that data)
    a = num//10
    b = num%10
    c = -1
    while num != 0:
        num //= 10
        c += 1
    return b*10**c + a
# print(code(12345))

# ---Loops---
# --Oski Stole Your Power--
def power(x,y): # works for positive and negative integers and zero
    if y != 0:
        b = abs(y)-1
        a = x
        while b != 0:
            a *= x
            b -= 1
        if y > 1:
            return a
        else: return 1/a
    else: return 1
# print(power(-2,-3))

# --Min and Max with Loops!--
# -For Loops-
# list = [-5, 1, 6, 24, -15, 8, 14]
def minimum_f(list):
    a = list[0]
    for num in list:
        if num < a:
            a = num
    return a
# print(minimum(list))
def maximum_f(list):
    a = list[0]
    for num in list:
        if num > a:
            a = num
    return a
# print(maximum(list))

# -While Loops-
# list = [-5, 1, 6, 24, -15, 8, 14]
def minimum_w(list): # I think this is a stupid solution but it works
    a = 0 
    b = 0
    while b < len(list)-1: # This pretty much just checks "for all values in list"
        b += 1
        if list[a] > list[b]:
            a = b
    return list[a]
# print(minimum(list))
def maximum_w(list):
    a = 0 
    b = 0
    while b < len(list)-1:
        b += 1
        if list[a] < list[b]:
            a = b
    return list[a]
# print(maximum(list))

# --calculate Sum--
# num = -2468 
def sum(num):
    a = 0
    num = abs(num) # abs so it works for negatives
    while num > 0:
        a += num%10
        num //= 10
    return a
# print(sum(num))

# x = 123456
# result = code(x) # moves the last digit of x to the front

# print(f"The result of Secret Code (5.4) with x = {x} is {result}")