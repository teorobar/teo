# File: homework1.py

# --- Variables and Data Types ---

a=10
print(a)
print(type(a)) # a is an int, or integer, a whole number with no decimals

b=1.5
print(b)
print(type(b)) # b is a float, or floating-point number, a number with a decimal point or a fraction

c=3j
print(c)
print(type(c)) # c is a complex, or complex number, a number with a real component and an imaginary component

d="hello"
print(d)
print(type(d)) # d is a str, or string, a sequence of letter or characters contained in quotes

e=[1,2,3]
print(e)
print(type(e)) # e is a list, a sequence of various data types enclosed in brackets

f={"name":"Ellen","favorite fruit":"strawberry"}
print(f)
print(type(f)) # f is a dict, or dictionary, a list of pairs of data enclosed in curly braces

g=(1,2)
print(g)
print(type(g)) # g is a tuple, a sequence of various data types enclosed in parentheses that are not changeable

h=["apple","bananna","strawberry"]
print(h)
print(type(h)) # h is a list, a sequence of various data types enclosed in brackets

i=True
print(i)
print(type(i)) # i is a bool, or boolean, representing a binary True or False

j=None
print(j)
print(type(j)) # j is a nonetype, representing the absence of any value

k=[True,"blue",12]
print(k)
print(type(k)) # k is a list, a sequence of various data types enclosed in brackets

l=str(14) # note: str() was sued to convert the int 14 into its corresponding string form
print(l)
print(type(l)) # l is a str, or  string, a sequence of letter or characters contained in quotes

m=1e4 # note: python interprets <a>e<b> as scientific notation
print(m)
print(type(m)) # m is a float, or floating point number, a number with a decimal point or a fraction

# Question 5
n=range(6)
print(n)
print(type(n)) # n is a range, a sequence of integers 0 through n-1

'''
1. I found 9 unique data types.
2. int, float, complex, str, list, dict, tuple, bool, and nonetype.
3. b and m are both floats. e, h , and k are all lists. d and l are both strings.
4. l is a string. It is not an integer because it was defined using str(), which turns a data type into its corresponding string form.
5. (See Question 5 or n)
'''

# --- Booleans ---

print(10>9) # True, 10 is greater than 9

print(10==9) # False, 10 does not equal 9

print(10<=9) # False, 10 is not less than or equal to 9

print(bool("abc")) # True, not empty set

print(bool(123)) # True, non-zero number

print(bool(["apple","cherry","banana"])) # True, not empty set

print(bool(True)) # True, defined to be True

print(bool(False)) # False, defined to be False

print(bool(0)) # False, 0 is synonymous to False

print(bool("")) # False, empty set

print(bool(" ")) # True, not empty set

print(bool(())) # False, empty set

print(bool([])) # False, empty set

print(bool({})) # False, empty set

print(bool(True and False)) # False, and operator returns False if either value is False

print(bool(True and True)) # True, and operator returns True since neither value is False

print(bool(False and False)) # False, and operator returns False since both values are False

print(bool(True or False)) # True, or operator returns True if either value is True

print(bool(True or True)) # True, or operator returns True since both values are true

print(bool(False or False)) # False, or operator return False since neither vlue is True

print(bool(not(False))) # True, defined to be the opposite of false

print(bool(not(True))) # False, defined to be the opposite of true

# Question 3
print(bool("False")) # True, this is technically a non-empty string so it is True even though the string reads "False"

# Question 4
print(bool(0.0)) # False, this still has a value of 0 even though it is a float rather than an int

'''
1. False is generally represented by the value False, 0, empty sets, or untrue mathematical equations. Everything else is true for the most part.
2. I was a bit surprised about how the and and or operators functioned since they seem rather nonsensical in this context.
3. (See Question 3)
4. (See Question 4)
'''

# --- Operators ---

# -- Arithmetic Operators --

print(10+5) # 15, + performs addition

print(10-5) # 5, - performs subtraction

print(2*4) # 8, * performs multiplication

print(6/3) # 2, / performs division

print(5%2) # 1, % solves for the remainder of a division operation

print(3**2) # 9, ** performs exponentiation

print(15//2) # 7, // performs division rounded to the next smallest whole number

# -- Comparison Operators --

print(5==2) # False, == means equal to

print(10!=10) # False, != means is not equal to

print(2<5) # True, < means is less than

print(5<=6) # True, <= means is less than or equal to

print(1>=10) # False, >= means is greater than or equal to

# -- Assignments Operators --

x=5

x+=5 # += performs addition and then sets the value equal to the sum
print(x) # 5 + 5 = 10

x-=4 # -= performs subtraction and then sets the value equal to the difference
print(x) # 10 - 4 = 6

x*=3 # *= performs multiplications and then sets the vaule equal to the product
print(x) # 6 * 3 = 18

# -- Logical Operators --

# 1. and outputs True only if all values are True and outputs False otherwise
print(bool(1 and True)) # True
print(bool(0 and 1)) # False

# 2. or outputs True if any values are True and outputs False otherwise
print(bool("Sol" or False)) # True
print(bool([] or '')) # False

# 3. not outputs the logical negation of the value
print(bool(not(0))) # True
print(bool(not([1]))) # False

'''
1. / gives the exact quotient as a float while // gives a rounded whole number quotient.
2. % gives the remainder of the division while // gives a rounded whole numebr quotient.
3. I would use % to calculate the remainder of a whole number division. e.g. 7 % 2 = 1
4. Assignment operators perform an operation on a variable and then assign the variable the new value.
'''

# --- Strings ---

my_string="hello"

print(my_string) # Prints: hello

print(my_string[0]) # Prints: h

print(my_string[1]) # Prints: e

print(my_string[2]) # Prints: l

print(my_string[3]) # Prints: l

print(my_string[4]) # Prints: o

print(my_string[-1]) # Prints: o

print(my_string[1:3]) # Prints: el

print(my_string[0:5:2]) # Prints: hlo

print(len(my_string)) # Prints: 5

print(my_string+"goodbye") # Prints: hellogoodbye

print(7*my_string) # Prints: hellohellohellohellohellohellohello

# Question 2:
name="Oski"
print("Hello, my name is", name)

# Question 3:
print(f"Hello, my name is {name}")

'''
1. slicing allows you to choose which elements in a set to include. I did this in my_string[1:3] and my_string[0:5:2]
2. The value of name was printed, finishing the sentence
3. The value of name was added to the string by adding f in front
4. The second statement used an f-string to embed the call name directly inside of the string before printing it
'''

# --- Terminal Commands ---

'''
1. cd
Changes directories. Use it to move from one folder to another
Example: cd Desktop

2. ls
Lists all files in directory
Example: ls homework1

3. ls -a
Lists all files in directory including hidden files
Example: ls -a homework1

4. mkdir
Makes a directory inside current directory
Example: mkdir homework1

5. cat
Displays content of text files
Example: cat homework1.py

6. pwd
Displays directory tree
Example: pwd

7. cd ..
Opens parent directory
Example: cd ..

8. cd .
Opens current directory
Example: cd .

9. cd ~
Opens home directory
Example: cd ~

10. cp
Creates a copy of a file
Example: cp homework1 homework1_final

11. mv
Renames a file or directory or moves or a file to a new directory
Example: mv homework1 homework1_final

12. rm
Removes a file or directory
Example: rm homework1

13. clear
Erases all previous output from the screen
Example: clear

14. grep
Prints lines that contain specified text
Example: grep "Oski" homework1.py
'''

'''
1. nano is used to edit code from the terminal. man accesses manual pages for a specific command. rmdir removes a directory.
2. ls -a shows hidden files that ls does not.
3. A hidden file is simply a file that is not displayed by default.
4. grep -v does the inverse of grep, identifying lines without specific text. -l prevides a longer format of the output with more detail. -f forces a command, bypassing warnings
'''